echo "Running tests"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)

# pytest
find $DIR/src/tests -type f -not -path "*/__pycache__/*" -not -path "*/.pytest_cache/*"  -exec pytest {} +
