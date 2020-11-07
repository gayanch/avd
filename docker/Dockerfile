FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install --no-install-recommends -y git python3 python3-pip
RUN mkdir app

RUN apt-get install -y python3-dev
RUN apt-get install -y build-essential
WORKDIR /app
RUN git clone https://github.com/gayanch/avd

WORKDIR /app/avd
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "uwsgi", "--ini", "/app/avd/avd.ini" ]