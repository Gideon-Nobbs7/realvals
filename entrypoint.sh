#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput


python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Start the Django server
exec python manage.py runserver 0.0.0.0:8000