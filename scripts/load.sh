# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))
DIR=$(dirname $CURRENT_DIR)
VENVDIR=${1:-$DIR/venv}

# recursively source scripts
for f in $(find $CURRENT_DIR/functions -type f); do
	source $f
done

# alias for common developer commnads
alias dos2unix="find ${DIR} -type f  -not -path '*/node_modules*' -not -path '*/venv/*'  -exec dos2unix {} +"
alias venv="source ${VENVDIR}/bin/activate"
alias build="source ${CURRENT_DIR}/build.sh"
alias format="black $DIR/src/backend/ $DIR/src/wsgi.py $DIR/src/tests/"
alias rundocker="docker exec -it ati-project_web_1 bash"
alias runserver="FLASK_APP=${DIR}/src/wsgi.py FLASK_ENV=development flask run --reload -h 0.0.0.0 -p 8080"
alias extract_text="pybabel extract -F $DIR/src/babel.cfg -k lazy_gettext -o $DIR/src/translations/messages.pot $DIR/src"
alias update_translation="pybabel compile -i $DIR/src/translations/messages.pot -o $DIR/src/translations"
alias generate_language="pybabel init -i $DIR/src/translations/messages.pot -d $DIR/src/translations -l"
alias translate="pybabel compile -d $DIR/src/translations"
alias run="yarn run dev"
