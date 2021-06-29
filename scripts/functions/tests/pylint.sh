function run_pylint {
	pylint -j 0 --output-format=colorized $DIR/src/
}
