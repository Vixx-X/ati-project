echo "


                 █████╗ ████████╗██╗                      
                ██╔══██╗╚══██╔══╝██║                      
                ███████║   ██║   ██║                      
                ██╔══██║   ██║   ██║                      
                ██║  ██║   ██║   ██║                      
                ╚═╝  ╚═╝   ╚═╝   ╚═╝                      
                                                          
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                          


"

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))

DIR=$(dirname $CURRENT_DIR)
VENVDIR="${1:-$DIR/venv}"

# initial setup on Postgres DB
function setup_db {
	echo "Done"
}

# setup initial venv and pip install the project
function setup_venv {
	python3 -m venv $VENVDIR
	source ${VENVDIR}/bin/activate
	echo "virtual enviroment activated"

	echo "updating pip"
	python3 -m pip install --upgrade pip
	echo "pip installing"
	pip install -r requirements/prod.txt -r requirements/dev.txt
}

# recursively source scripts
for f in $(find $CURRENT_DIR/functions -type f); do
	source $f
done

# alias for common developer commnads
alias venv="source ${VENVDIR}/bin/activate"
alias build="${CURRENT_DIR}/build.sh"
alias format="black ${DIR}/src"

source $CURRENT_DIR/test.sh

function help {
	echo "venv           - activate virtualenv (if needed)"
	echo ""
	echo "setup_venv     - initial venv and pip install the project"
	echo "setup_db       - initial db setup"
	echo ""
	echo "build          - build and minify both css and js files"
	echo "autodocs       - build automatic documentation"
	echo ""
	echo "black          - run formatter (black)"
	echo "runtests       - run pylint and pytest tests"
}

echo "All done!"

echo ""
echo "Your root directory is: ${DIR}"
echo "Your virtualenv directory is: ${VENVDIR}"

echo ""
echo "Use 'help' for list of commnads"
