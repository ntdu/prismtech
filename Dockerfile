FROM python:3.10.7-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN mkdir -p /app/statics /app/log/{uwsgi,gunicorn,uvicorn}

COPY requirements.txt /app/

# Updating repository sources
RUN apt-get update  -y \
    && apt-get clean

RUN apt-get install make
RUN apt-get install g++ -y

# Debian modules for postgress
RUN apt-get install -y libpq-dev && apt-get install -y gcc

RUN pip3 install -r requirements.txt

COPY . /app/