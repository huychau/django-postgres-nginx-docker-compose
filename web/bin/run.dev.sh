#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn -c gunicorn_conf.py config.wsgi:application --reload
