FROM python:3.9.5-alpine3.13

WORKDIR /code
COPY requirements/prod.txt /requirements.txt
COPY src/backend backend
COPY src/static static
COPY src/templates templates
COPY src/translations translations
COPY src/config config
COPY src/wsgi.py .

RUN apk add --update-cache && \
    apk add --update alpine-sdk && \
    apk add libffi-dev openssl-dev && \
    apk add bash && \
    apk --no-cache --update add build-base && \
    apk add --update nodejs nodejs-npm

# Yarn should already be built before building this image

RUN pip install -U pip
RUN pip install -r /requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["prod"]

