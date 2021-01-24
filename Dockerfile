FROM python:3.9.1-buster

ADD example /tmp/example
WORKDIR /tmp/example

RUN apt update && \
    apt install libpq-dev && \
    python -m pip install psycopg2 Django djangorestframework gunicorn
