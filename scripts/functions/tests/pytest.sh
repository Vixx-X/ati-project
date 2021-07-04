function run_pytest {
	find $DIR/src/tests -type f -not -path "*/__pycache__/*" -not -path "*/.pytest_cache/*"  -exec pytest {} +
}
