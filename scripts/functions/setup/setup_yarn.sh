# setup yarn (it just yarn install)
function setup_yarn {
	cd $DIR
	node -v >/dev/null 2>&1
	if [ $? -ne 0 ]; then
		echo "Please install node"
		cd -
		return
	fi
	yarn -v >/dev/null 2>&1
	if [ $? -ne 0 ]; then
		echo "Please install yarn"
		cd -
		return
	fi
	yarn install
	cd -
}
