echo "Running linter"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)

# pylint
pylint -j 0 --output-format=colorized $DIR/src/backend/ $DIR/src/wsgi.py $DIR/src/tests/
