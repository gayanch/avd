FROM ubuntu:20.04

RUN apt update && \
    apt install git python3 python3-pip
RUN mkdir app

WORKDIR /app
RUN git clone https://github.com/gayanch/avd

WORKDIR /app/avd
RUN pip install -r requirements.txt
ENTRYPOINT [ "uwsgi", "--ini", "/app/avd/avd.ini" ]