# Django-occurrence-logger

[![License](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com)

Django-occurrence-logger is a django-based web application to report city related events and their respective locations.

---

# Stack

> Django, PostgreSQL w/ PostGIS, Docker

---

# Instructions

Requires the use of [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

## Clone from repository
```sh
$ git clone https://github.com/gmpmagalhaes/django-occurrence-logger
```

**In order for geopy to be able to convert an adress to a location, a google maps API enabled application name must be provided.
Please create an environment file in the root of the project with an appropriate app name. See below:**
```sh
$ cd django-occurrence-logger
$ echo "GOOGLE_APPNAME=<your_app_name_goes_here>" > ./backend/.env
```

## Start Docker
Assuming you have docker installed. 
:exclamation: You might need to run the docker commands with sudo privileges, depending on how you've setup docker.
Example: ```$ sudo docker-compose build ```

```sh
$ cd django-occurrence-logger # if not in root from previous step
# build the docker image and start the container
$ docker-compose build && docker-compose up -d
# run the migrations
$ docker-compose exec server python manage.py makemigrations
$ docker-compose exec server python manage.py migrate
```
Both the server and database should be running on the background now.
Check if running with:
```sh
$ docker ps
# if not running, check logs
$ docker-compose logs
```

## All set!
Navigate to the server address in your browser of choice.
```sh
localhost:8000
# or
127.0.0.1:8000
```

---

# Follow the wiki for more information on the API Endpoints

**_Please read the wiki for further information. [Wiki](https://github.com/gmpmagalhaes/django-occurrence-logger/wiki/Home)_**


# License

This project is available under the [MIT License](https://github.com/gmpmagalhaes/django-occurrence-logger/blob/master/LICENSE.md)
