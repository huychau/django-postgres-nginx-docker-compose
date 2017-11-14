#!/bin/sh

python manage.py makemigrations
python manage.py migrate
gunicorn -c gunicorn_conf.py config.wsgi:application --reload
# gunicorn config.wsgi:application -w 2 -b 0.0.0.0:8000 --reload
# python manage.py runserver 0.0.0.0:8000
