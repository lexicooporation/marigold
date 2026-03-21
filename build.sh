#!/usr/bin/env bash
set -e

pip install -r requirements.txt
cd marigoldsite
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --no-input