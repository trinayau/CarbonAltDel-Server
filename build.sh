#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# Run the project
echo "Make migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static files"
python3.9 manage.py collectstatic --noinput --clear

# echo "create superuser"
# python3.9 manage.py createsuperuser --noinput
