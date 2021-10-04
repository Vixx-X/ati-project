FROM python:3.9.5-alpine3.13

WORKDIR /code
COPY requirements /requirements

# apk --no-cache --update add build-base && \
RUN apk add --update-cache && \
    apk add --update alpine-sdk && \
    apk add --update libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl && \
    apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev && \
    apk add bash && \
    apk add --update yarn

RUN pip install -U pip
RUN pip install -r /requirements/prod.txt -r /requirements/dev.txt

# RUN yarn install
# RUN yarn build

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["dev"]

