FROM python:3.9.5

WORKDIR /code
COPY requirements/prod.txt prod.txt
COPY requirements/dev.txt dev.txt
RUN pip install -r prod.txt -r dev.txt

COPY src/ .

CMD python wsgi.py
