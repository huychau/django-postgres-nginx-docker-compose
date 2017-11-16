#!/bin/sh

# Migrating data
./manage.py makemigrations
./manage.py migrate

# Running Gunicorn server
gunicorn -c gunicorn_conf.py config.wsgi:application --reload
