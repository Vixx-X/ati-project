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
