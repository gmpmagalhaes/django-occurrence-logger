FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api

RUN apt update && apt install -y gdal-bin libgdal-dev python-gdal binutils python-psycopg2

COPY . /api/

COPY manage.py requirements.txt /api/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

