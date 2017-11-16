#!/bin/sh

coverage run --source='.' manage.py test
coverage html
cd htmlcov/
python -m http.server 8080
