echo "Bringing docker files"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)
source $CURRENT_DIR/load.sh

if [ "$1" = 'dev' ]; then
	# Use dev docker files
	setup_dev
elif [ "$1" = 'prod' ]; then
	# Use prod docker files
	setup_prod
fi

