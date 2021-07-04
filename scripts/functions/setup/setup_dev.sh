function setup_dev {
	# Use dev docker files
	cd $DIR && \
	if [ -d db ]; then
		echo "Do you want to delete the db (will need sudo)? (y/N)"
		read -q && sudo rm -rf db || :
	fi
	cp docker/dev/* . && \
	docker-compose build && \
	docker-compose up -d && \
	cd  -
}
