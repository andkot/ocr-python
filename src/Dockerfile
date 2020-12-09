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


COPY . ./src

#CMD ["python3", "src/tesser_api.py"]
ADD run.sh /
RUN chmod +x /run.sh

CMD ["/run.sh"]