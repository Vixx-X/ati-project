function setup_prod {
	# Use prod docker files
	cd $DIR && \
	cp docker/prod/* . && \
	cd  -
}
