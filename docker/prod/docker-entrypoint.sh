#!/usr/bin/env sh
set -e

if [ "$1" = 'prod' ]; then
	# Start app
	echo "Staring app"
	gunicorn project.wsgi:application --bind 0.0.0.0:5000 --timeout 300
fi

exec "$@"


