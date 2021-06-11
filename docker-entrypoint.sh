#!/usr/bin/env bash
set -e

if [ "$1" = 'project' ]; then
	# Start app
	python app.py
fi

exec "$@"


