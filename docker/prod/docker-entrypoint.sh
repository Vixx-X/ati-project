#!/usr/bin/env sh
set -e

if [ "$1" = 'project' ]; then
	# Start app
	python app.py
fi

exec "$@"


