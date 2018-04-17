#!/bin/bash

set -e

# Apply database migrations
echo "Apply database migrations"
while ! python manage.py migrate --noinput 2>&1; do
  echo "⏳ Waiting on DB..."
  sleep 3
done

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
if [ "$APP_ENV" = 'dev' ]
then
#    echo "Load fixture"
#    python manage.py loaddata fixtures/dump.json

    echo "Running Development Server"
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "Running Production Server"
    exec uwsgi --ini uwsgi.ini
fi
