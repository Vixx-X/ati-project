FROM python:3.9.5-alpine3.13

WORKDIR /code
COPY requirements.txt .
COPY src .
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["project"]
