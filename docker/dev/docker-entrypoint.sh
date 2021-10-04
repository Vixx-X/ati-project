#!/usr/bin/env sh
set -e

if [ "$1" = 'dev' ]; then

	echo "Building static files"
	# yarn build

	echo "Loading fixtures"
	FLASK_APP=src/wsgi.py FLASK_ENV=development flask loaddata ./fixture

	echo "Staring app"
	FLASK_APP=src/wsgi.py FLASK_ENV=development flask run --reload -h 0.0.0.0 -p 5000
fi

exec "$@"


