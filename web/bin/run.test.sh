#!/bin/sh

# Migrating data
./manage.py makemigrations
./manage.py migrate

coverage run --source='.' manage.py test
coverage html
cd htmlcov/
python -m http.server 9000
