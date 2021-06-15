#!/usr/bin/env sh
set -e

if [ "$1" = 'dev' ]; then
	# Start app
	FLASK_APP=src/app.py flask run --reload -h 0.0.0.0 -p 5000
fi

exec "$@"


