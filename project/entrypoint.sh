#! /usr/bin/env sh
set -e

/uwsgi-nginx-flask-entrypoint.sh

python create_models.py

exec "$@"
