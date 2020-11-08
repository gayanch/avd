FROM alpine:latest as builder
RUN apk add --update python3 git python3-dev alpine-sdk linux-headers

WORKDIR /app
RUN git clone https://github.com/gayanch/avd.git

WORKDIR /app/avd
RUN python3 -m venv appenv \
    && source appenv/bin/activate \
    && pip install -r requirements.txt 

FROM alpine:latest
COPY --from=builder /app /app
RUN apk add --update python3 \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup \
    && chown -R appuser:appgroup /app 
WORKDIR /app/avd
USER appuser
ENTRYPOINT [ "sh", "startavd.sh" ]
