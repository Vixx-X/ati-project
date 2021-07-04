echo "Running tests"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)
source $CURRENT_DIR/load.sh

# pytest
run_pytest
