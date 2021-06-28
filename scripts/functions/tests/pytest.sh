function run_pytest {
	find $DIR/src -type f -not -path "*/__pycache__/*" -not -path "*/.pytest_cache/*"  -exec pytest {} +
}
