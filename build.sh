#!/usr/bin/env bash
# exit on error
set -o errexit

echo "==> Installing Python dependencies..."
pip install -r requirements.txt

echo "==> Collecting static assets..."
python manage.py collectstatic --noinput

echo "==> Running database migrations..."
python manage.py migrate --noinput

echo "==> Seeding initial fixtures and admin..."
python manage.py seed_data

echo "==> Build completed successfully!"
