#!/usr/bin/env bash
set -e # exit if the is an error

if [ "$1" = 'dev' ]; then
	# Use dev docker files
	sudo rm -rf db
	cp docker/dev/* .
	docker-compose build
	docker-compose up -d
elif [ "$1" = 'prod' ]; then
	# Use prod docker files
	cp docker/prod/* .
fi

