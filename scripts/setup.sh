source ./load.sh

if [ "$1" = 'dev' ]; then
	# Use dev docker files
	setup_dev
elif [ "$1" = 'prod' ]; then
	# Use prod docker files
	setup_prod
fi

