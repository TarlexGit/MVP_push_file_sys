#!/bin/sh
sleep 2;

python manage.py grpcrunserver & python manage.py runserver 0.0.0.0:8000 