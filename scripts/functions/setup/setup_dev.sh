function setup_dev {
	# Use dev docker files
	echo "Do you really want to start the container? (y/N)"
	read -q || return 0
	echo "" && \
	cd $DIR && \
	if [ -d db ]; then
		echo "Do you want to delete the db? (will need sudo) (y/N)"
		read -q && sudo rm -rf db || :
	fi
	source ./env/.env || echo "/env/.env not found"
	cp docker/dev/* . && \
	DB_USERNAME=$DB_USERNAME DB_PASSWORD=$DB_PASSWORD docker-compose build && \
	DB_USERNAME=$DB_USERNAME DB_PASSWORD=$DB_PASSWORD docker-compose up -d
	cd  -
}
