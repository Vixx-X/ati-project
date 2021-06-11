FROM python:3.8.5-alpine3.12

WORKDIR /code
COPY requirements.txt .
COPY src .
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["project"]
