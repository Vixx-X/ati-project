function run_pylint {
	pylint -j 0 --output-format=colorized --fail-under=8.0 $DIR/src/backend/ $DIR/src/wsgi.py $DIR/src/tests/
}
