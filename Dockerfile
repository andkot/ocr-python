# set base image
FROM python:3.8-alpine

ARG VCS_REF
ARG BUILD_DATE

# Create our tesseract user
RUN addgroup -g 1000 -S tesseract \
      && adduser -u 1000 -S -h /tesseract -s /bin/sh -G tesseract tesseract

# Install all needed runtime dependencies.
RUN set -xe; \
      apk add --update --no-cache --virtual .runtime-deps \
          bash \
          cairo \
          giflib \
          icu \
          libjpeg-turbo \
          libpng \
          libwebp-dev \
          openjpeg \
          pango \
          tiff \
          zlib; \
      apk add --no-cache --virtual .build-deps \
          alpine-sdk \
          autoconf \
          automake \
          cairo-dev \
          giflib-dev \
          git \
          icu-dev \
          libjpeg-turbo-dev \
          libpng-dev \
          libtool \
          libwebp-dev \
          openjpeg-dev \
          pango-dev \
          tiff-dev \
          zlib-dev; \
      cd /var/tmp; \
      wget http://www.leptonica.org/source/leptonica-1.75.3.tar.gz; \
      tar xfv leptonica-1.75.3.tar.gz; \
      rm leptonica-1.75.3.tar.gz; \
      cd leptonica-1.75.3; \
      ./configure --prefix=/usr/local/; \
      make; \
      make install; \
      cd /var/tmp; \
      rm -rf leptonica-1.75.3; \
      git clone https://github.com/tesseract-ocr/tesseract.git; \
      cd tesseract; \
      git checkout 3.05.01; \
      ./autogen.sh; \
      ./configure --prefix=/usr/local/; \
      make; \
      make install; \
      cd /var/tmp; \
      rm -rf tesseract; \
      mkdir -p /tesseract/tessdata; \
      cd /tesseract/tessdata/; \
      wget https://github.com/tesseract-ocr/tessdata/raw/3.04.00/eng.traineddata; \
      cd /; \
      chown -R tesseract:tesseract /tesseract; \
      apk del .build-deps;

# Copy our docker assets.
# COPY ./docker-entrypoint.sh /usr/local/bin/entrypoint.sh

# Drop down to our unprivileged user account.
# USER tesseract

# Set our working directory.
WORKDIR /tesseract

# Set our environment variables.
ENV TESSDATA_PREFIX=/tesseract/tessdata

# Setup the data volume.
VOLUME ["/tesseract/data"]

# =====================================
# RUN tesseract -v
#FROM python:3.8-alpine
RUN tesseract -v

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## set working derictory in container
#WORKDIR /app

# copy and run the dependencies file to the working directory
COPY req.txt .
# install openblas

RUN apk update \
    && apk add --upgrade --no-cache \
        bash openssh curl ca-certificates openssl less htop \
		g++ make wget rsync \
        build-base libpng-dev freetype-dev libexecinfo-dev openblas-dev libgomp lapack-dev \
		libgcc libquadmath musl  \
		libgfortran \
		lapack-dev \
	&&  pip install --no-cache-dir --upgrade pip \
	&&  pip install numpy==1.17.3 \
	&&  pip install scipy==1.3.1

ENV OPENCV_VERSION="4.5.0"
RUN apk add cmake
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
RUN unzip ${OPENCV_VERSION}.zip \
&& cd opencv-${OPENCV_VERSION}\
&& mkdir cmake_binary \
&& cd cmake_binary \
&& cmake -DBUILD_TIFF=ON \
  -DBUILD_opencv_java=OFF \
  -DWITH_CUDA=OFF \
  -DWITH_OPENGL=ON \
  -DWITH_OPENCL=ON \
  -DWITH_IPP=ON \
  -DWITH_TBB=ON \
  -DWITH_EIGEN=ON \
  -DWITH_V4L=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=$(python3.8 -c "import sys; print(sys.prefix)") \
  -DPYTHON_EXECUTABLE=$(which python3.8) \
  -DPYTHON_INCLUDE_DIR=$(python3.8 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON_PACKAGES_PATH=$(python3.8 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
  cd .. \
&& make install \
&& rm /${OPENCV_VERSION}.zip \
&& rm -r /opencv-${OPENCV_VERSION}
RUN ln -s \
  /usr/local/python/cv2/python-3.8/cv2.cpython-37m-x86_64-linux-gnu.so \
  /usr/local/lib/python3.8/site-packages/cv2.so

RUN pip3 install -r req.txt

# copy the content
COPY src/ .

# copy and make entrypoint.sh executable
COPY entpoint.sh .
RUN chmod +x ./entpoint.sh

# run
CMD ./entrypoint.sh

RUN tesseract -v





