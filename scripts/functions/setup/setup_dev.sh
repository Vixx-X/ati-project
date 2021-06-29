function setup_dev {
	# Use dev docker files
	cd $DIR && \
	if [ -d db ]; then
		while true; do
			read -p "Do you want to delete the db (will need sudo)?" yn
			case $yn in
				[Yy]* ) sudo rm -rf db && break;;
				[Nn]* ) break;;
				* ) echo "Please answer yes or no.";;
			esac
		done
	fi
	cp docker/dev/* . && \
	docker-compose build && \
	docker-compose up -d && \
	cd  -
}
