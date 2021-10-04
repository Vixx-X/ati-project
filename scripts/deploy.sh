echo "Building prod image"

# building statics
yarn build

# docker
cp ../docker/prod/Dockerfile ../docker/prod/docker-entrypoint.sh .

# building image
docker build -t vixxadesso/ati .

# sending to docker hub
docker push vixxadesso/ati

