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
echo "${BASH_SOURCE[0]}"
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)

# load all functions
source $CURRENT_DIR/load.sh

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
	echo ""
	echo "setup_dev      - bring docker files and start dev workspace"
	echo "setup_db       - bring prod docker files (use in production)"
}

echo "All done!"

echo ""
echo "Your root directory is: ${DIR}"
echo "Your virtualenv directory is: ${VENVDIR}"

echo ""
echo "Use 'help' for list of commnads"
