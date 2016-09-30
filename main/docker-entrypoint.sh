#!/bin/bash

nc -vz postgres-server 5432

while [ $? -eq 1 ]; do
    echo Database not ready for connections
    echo Sleepiong 3 seconds then trying again...
    sleep 3
    nc -vz postgres-server 5432
done

echo Database is ready bub

python /var/hermes/manage.py makemigrations
python /var/hermes/manage.py migrate

gunicorn --workers 3 --bind 0.0.0.0:8000 $1.wsgi:application
