#!/bin/sh

# Migrating data
./manage.py collectstatic --noinput
./manage.py makemigrations
./manage.py migrate

# Load dumpdata
./manage.py loaddata data.json
