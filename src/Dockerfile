#FROM ubuntu:latest
#
#ENV DEBIAN_FRONTEND=noninteractive
#ARG VCS_REF
#ARG BUILD_DATE
#
## Create our tesseract user
#RUN groupadd -g 1000 tesseract_group \
#    && useradd -u 1000 -g 1000 -s /bin/sh tesseract_user
#
#RUN apt-get update && \
#    apt-get install -y git-core
#RUN apt-get install -y autoconf
#RUN apt-get install automake
#RUN apt-get install -y git
#RUN apt-get install libpng-dev \
#    libtool \
#    libwebp-dev \
#    -y make \
#    -y cmake \
#    wget
#RUN cd /var/tmp; \
#    wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz; \
#    tar xfv leptonica-1.79.0.tar.gz; \
#    rm leptonica-1.79.0.tar.gz; \
#    cd leptonica-1.79.0; \
#    ./configure \
#    make; \
#    make install; \
#    cd /var/tmp; \
#    rm -rf leptonica-1.75.3; \
#    git clone https://github.com/tesseract-ocr/tesseract.git; \
#    cd tesseract; \
#    git checkout 3.05.01
#
#RUN cd var/tmp/tesseract; \
#    apt-get install gcc; \
#    apt-get -y install clang
#RUN apt-get install -y pkg-config
#RUN apt-get install -y libpango1.0-dev
#RUN apt-get install -y libicu-dev
#RUN apt-get install -y libcairo2-dev
#RUN apt-get install -y libleptonica-dev
#RUN cd var/tmp/tesseract; \
#    ./autogen.sh; \
#    ./configure
#
#RUN cd var/tmp/tesseract; \
#    make; \
#    make install; \
#
#RUN tesseract -v
#
##RUN cd var/tmp/tesseract; \
##    ldconfig
#
##RUN mkdir -p tesseract/tessdata; \
##    cd tesseract/tessdata/; \
##    wget https://github.com/tesseract-ocr/tessdata/raw/3.04.00/eng.traineddata
#
##RUN cd var/tmp/tesseract; \
##    ldconfig

# ====================================
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN set -xe \
    && echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y autoconf \
                          build-essential \
                          git \
                          libcairo2 \
                          libcairo2-dev \
                          libgomp1

RUN apt-get install -y libicu-dev \
                          libleptonica-dev \
                          libpango1.0-dev
RUN apt-get install automake libtool -y
RUN git clone https://github.com/tesseract-ocr/tesseract.git
RUN cd tesseract \
        && git checkout 3.05 \
        && ./autogen.sh \
        && ./configure \
        && make install
RUN ldconfig
RUN tesseract -v

RUN apt install -y python3-pip
RUN pip3 install pillow
RUN pip3 install opencv-python
RUN pip3 install pytesseract
RUN pip3 install tesserocr
RUN pip3 install pdf2image
RUN apt install wget

RUN cd tesseract \
    && make training \
    && make training-install

#RUN mkdir -p home/my_data/tessdata \
#    && cd home/my_data/tessdata \
#    && wget https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata \
#    && wget https://github.com/tesseract-ocr/tessdata/blob/master/pdf.ttf
##    && wget https://github.com/tesseract-ocr/tessdata/blob/master/tessconfigs \
##    && wget https://github.com/tesseract-ocr/tessdata/blob/master/configs

#VOLUME ['/home/andrei/my-space/prog/tessdata_2']

COPY . ./src

#RUN cd src/tessdata_2 \
#    && pwd \
#    && ls

RUN cd src \
    && python3 tesser_api.py