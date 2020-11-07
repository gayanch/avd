FROM alpine:latest as builder
RUN apk add --update python3 git python3-dev alpine-sdk linux-headers

WORKDIR /app
RUN git clone https://github.com/gayanch/avd

WORKDIR /app/avd
RUN python3 -m venv appenv \
    && source appenv/bin/activate \
    && pip install -r requirements.txt 

FROM alpine:latest
RUN apk add --update python3
COPY --from=builder /app /app
WORKDIR /app/avd
RUN source appenv/bin/activate
ENTRYPOINT [ "sh", "startavd.sh" ]
# FROM ubuntu:20.04

# RUN apt-get update && \
#     apt-get install --no-install-recommends -y git python3 python3-pip
# RUN mkdir app

# RUN apt-get install -y python3-dev
# RUN apt-get install -y build-essential
# WORKDIR /app
# RUN git clone https://github.com/gayanch/avd.git

# WORKDIR /app/avd
# RUN pip3 install -r requirements.txt
# ENTRYPOINT [ "uwsgi", "--ini", "/app/avd/avd.ini" ]