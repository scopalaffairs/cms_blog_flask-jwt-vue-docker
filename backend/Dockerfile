FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3 \
    python3-pip \
    python3-tk \
    python3-dev \
    libmagickwand-dev

RUN pip3 install --upgrade pip==9.0.3 \
    && pip3 install setuptools

ADD ./app /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV PYTHONPATH /usr/lib/python3
