FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y gdal-bin libgdal-dev python-gdal binutils python-psycopg2

COPY . /app/

COPY manage.py requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

