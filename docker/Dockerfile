FROM alpine:latest

RUN apk add python3 git py3-pip
RUN mkdir app

WORKDIR /app
RUN git clone https://github.com/gayanch/avd

WORKDIR /app/avd
RUN pip install -r requirements.txt
ENTRYPOINT [ "uwsgi", "--ini", "/app/avd/avd.ini" ]