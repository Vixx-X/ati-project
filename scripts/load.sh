# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)
VENVDIR="${1:-$DIR/venv}"

# recursively source scripts
for f in $(find $CURRENT_DIR/functions -type f); do
	source $f
done

# alias for common developer commnads
alias venv="source ${VENVDIR}/bin/activate"
alias build="${CURRENT_DIR}/build.sh"
alias format="black ${DIR}/src"

# load util base functions
source $CURRENT_DIR/test.sh

