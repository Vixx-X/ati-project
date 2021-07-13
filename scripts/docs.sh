echo "Building docs"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)

sphinx-apidoc -o ${DIR}/docs/source ${DIR}/src

