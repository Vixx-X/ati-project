FROM python:3.9.5-alpine3.13

WORKDIR /code
COPY requirements /requirements
RUN pip install -r /requirements/dev.txt -r /requirements/prod.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["dev"]

