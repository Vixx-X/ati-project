function setup_prod {
	# Use prod docker files
	cd $DIR && \
	source ./env/.env || echo "/env/.env not found"
	cp docker/prod/docker-compose.yaml . && \
	DB_USERNAME=${DB_USERNAME} DB_PASSWORD=${DB_PASSWORD} docker-compose up -d
	cd  -
}
