function run_pylint {
	pylint -j 0 --output-format=colorized $DIR/src/backend/ $DIR/src/wsgi.py $DIR/src/tests/
}
