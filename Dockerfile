FROM ubuntu:14.04

MAINTAINER Allen Sun allen.sun@daocloud.io

RUN sed -i "s/archive\.ubuntu\.com/mirrors\.163\.com/g" /etc/apt/sources.list \
        && apt-get update \
        && apt-get install -y python \
        && apt-get install -y python-pip \
        && pip install -i http://pypi.douban.com/simple requests \
        && apt-get clean

COPY ./sine.py /sine.py

EXPOSE 80

CMD ["python", "/sine.py"]