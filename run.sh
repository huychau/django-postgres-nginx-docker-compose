#!/bin/sh

python manage.py makemigrations
python manage.py migrate
gunicorn -c gunicorn_conf.py --chdir web config.wsgi:application --reload
