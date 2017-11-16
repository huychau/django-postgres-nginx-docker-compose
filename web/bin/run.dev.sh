#!/bin/sh

# Running Gunicorn server
gunicorn -c gunicorn_conf.py config.wsgi:application --reload
