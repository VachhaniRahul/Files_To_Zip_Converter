#!/bin/bash
set -o errexit  # Stop script on error

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py makemigrations fileapp
python manage.py migrate

# Automatically create superuser if CREATE_SUPERUSER is set
