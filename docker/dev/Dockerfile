FROM python:3.9.5-alpine3.13

WORKDIR /code
COPY requirements /requirements

RUN apk add --update-cache && \
    apk add --update alpine-sdk && \
    apk add libffi-dev openssl-dev && \
    apk add bash && \
    apk --no-cache --update add build-base

ENV ALPINE_MIRROR "http://dl-cdn.alpinelinux.org/alpine"
RUN echo "${ALPINE_MIRROR}/edge/main" >> /etc/apk/repositories && \
    apk add --no-cache nodejs-current  --repository="http://dl-cdn.alpinelinux.org/alpine/edge/community"

RUN pip install -r /requirements/dev.txt -r /requirements/prod.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["dev"]

