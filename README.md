# Ati Project

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents

- [Install pre-installation dependencies](#install-pre-installation-dependencies)
- [Setup MongoDB (database)](#setup-mongodb-database)
  - [Create .env file](#create-env)
  - [Setup dev enviroment](#setup-dev-env)
  - [Setup de Database and start the project](#create-a-database-and-database-user-for-development)
  - [Create and activate virtual enviroment and install python dependencies](#create-a-virtual-enviroment)
  - [Test the setup](#test-the-setup)
- [Developing Javascript and CSS](#developing-js-css)
- [Autodocumentation](#autodocumentation)
- [API documentation](#api-docs)
- [References](#references)

## Install pre-installation dependencies <a name="install-pre-installation-dependencies"></a>

- Python3
  Should come preinstalled with Ubuntu.

- Pip3 and NodeJs
  Installation on Ubuntu
  `sudo apt install python3-venv python3-pip nodejs npm`

- Install yarn the package manager for nodejs
  `npm install --global yarn`

- Docker
  [Installation on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  [Other OS or distros](https://docs.docker.com/engine/install/)

- Use mongo from docker
  `docker run --name mongo -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=1234 -p 27017:27017 -d mongo`
- Use mongo shell from mongo image
  `docker run -it --rm --name mongo-shell --net=host mongo mongo`

## Setup MongoDB (database) <a name="setup-mongodb-database"></a>

_WIP_
`sudo apt-get install mongo`

## Create .env file <a name="create-env"></a>

_WIP_
Edit `.env.example` with your own settings and rename it `.env`

## Setup dev enviroment <a name="setup-dev-env"></a>

```bash
source ./scripts/start.sh

setup_dev

rundocker
```

Inside the container, you could access all the tooling repeating this command:

```bash
source ./scripts/start.sh
```

### Create and activate virtual enviroment and install python dependencies (Optional)<a name="create-a-virtual-enviroment"></a>

If you would like to not use Docker, you could use virtualenv as so:

```bash
setup_venv
```

### Setup de Database and start the project <a name="create-a-database-and-database-user-for-development"></a>

_WIP_

```bash
setup_db
```

### Install nodejs packages

```bash
yarn install
```

### Test the setup <a name="test-the-setup"></a>

Test the setup by running the development server

```bash
runserver
```

Or test that all of the development processes work (this will run frontend and backend)

```bash
run
```

## Developing Javascript and CSS <a name="developing-js-css"></a>

Detailed documentation about npm scripts and the workflow of developing `js` and `css` can be found [here](./docs/development_process.md)

## API documentation <a name="api-docs"></a>

Documentation can be found in the url `api/schema/swagger-ui/` and `schema/redoc/`. You'll be to need authenticated as admin.

## Autodocumentation <a name="autodocumentation"></a>

### Generate Documentation for Web

We are using Sphinx to generate an html documentation from docstring inside your code run, to make the docs, run:

```bash
autodocs
```

Then build the html by doing:

```bash
build_docs
```

Your html documentation will end up in the `docs/build/html/index.html`.

```bash
$BROWSER docs/build/html/index.html
```

Config settings are in the file `docs/conf.py`

[Find out more about Sphinx][sphinx]

## References <a name="references"></a>

- [Steps followed to setup flask with mongodb][mongodb]
- [Directory structure explanation](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)

[mongodb]: https://flask-user.readthedocs.io/en/latest/mongodb_app.html
[sphinx]: https://www.sphinx-doc.org/en/master/
