#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# seed data
python manage.py seed seed_data/consumers.csv
