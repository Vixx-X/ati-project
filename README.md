# Ati Project

<desc>
  
For the ATI related stuff already knowing the project, fell free to [skip](#ita).

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents

- [Install pre-installation dependencies](#install-pre-installation-dependencies)
- [Setup MongoDB (database)](#setup-mongodb-database)
- [Create .env file](#create-env)
- [Setup dev enviroment](#setup-dev-env)
  - [Using docker and docker-compose]("#dev-docker")
  - [Create and activate virtual enviroment and install python dependencies (optional)](#create-a-virtual-enviroment)
- [Developing Javascript and CSS](#developing-js-css)
- [Test the setup](#test-the-setup)
- [Documentation](#docs)
  - [Autodocumentation](#autodocumentation)
  - [API documentation](#api-docs)
- [Testing](#tests)
  - [Run Pylint](#pylint-tests)
  - [Unit and Integration tests with Selenium](#selenium-tests)
- [ITA Course](#ita)
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


## Setup MongoDB (database) <a name="setup-mongodb-database"></a>

- MongoDB
  [Installation on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
  [Other OS or distros](https://docs.mongodb.com/manual/administration/install-community/)
  
- Use mongo from docker (preferably)
  `docker run --name mongo -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=1234 -p 27017:27017 -d mongo`
  - Use mongo shell from mongo image
    `docker run -it --rm --name mongo-shell --net=host mongo mongo`
  

## Create .env file <a name="create-env"></a>

Inside `env` copy or edit `.env.example` with your own settings and rename it `.env` on the same directory.


## Setup dev enviroment <a name="setup-dev-env"></a>

### Using docker and docker-compose <a name="dev-docker"></a>

With this command, all the development docker enviroments will be copied to the root repo.

```bash
source ./scripts/start.sh

setup_dev
```

To start the enviroment, just run the next command:
```bash
rundocker
```

Inside the container, you could also access all the tooling repeating this command:

```bash
source ./scripts/start.sh
```

### Create and activate virtual enviroment and install python dependencies (Optional)<a name="create-a-virtual-enviroment"></a>

If you would like to not use Docker, you could also use virtualenv as so:

```bash
setup_venv
```

## Developing Javascript and CSS <a name="developing-js-css"></a>

Detailed documentation about npm scripts and the workflow of developing `js` and `css` can be found [here](./docs/frontend_development_process.md).

### Install yarn packages and build the static assets

Install js/css dependencies.
```bash
yarn install
```
  
Build statics files.
```bash
yarn build
```

## Test the setup <a name="test-the-setup"></a>

### Docker test
  
For whom using docker was their choice, just open up your browser on `http://127.0.0.1:5000/`

### Test the setup by running the development server

If you are using virtualnev, please run this, to start the flask server.

```bash
runserver
```

Or test that all of the development processes work (this will run frontend and backend)

```bash
run
```

## Generate Documentation for the Web <a name="docs"></a>

We are using Sphinx to generate our public html [documentation](https://docs.ati.vittorioadesso.com) from docstring inside your our code.

### Autodocumentation <a name="autodocumentation"></a>

To make the docs, just run:

```bash
autodocs
```

Then build the html by typing:

```bash
build_docs
```

Your html documentation will end up in the `docs/build/html/index.html`.

```bash
$BROWSER docs/build/html/index.html
```

Config settings are in the file `docs/conf.py`

[Find out more about Sphinx][sphinx]

### API documentation <a name="api-docs"></a>

Documentation can be found in the url `api/schema/swagger-ui/` and `schema/redoc/`. You'll be to need authenticated as admin.

## Testing the application <a name="tests"></a>

For testing we choose to use one of the most popular testing framework [Pytest][pytest]. But we also like to before, run our prefer linter [Pylint][pylint], to catch up for simple errors, and improve our code quality.
  
### Run Pylint <a name="pylint-tests"></a>

Running pylint is as simple as
```bash
run_pylint
```
  
### Unit and Integration tests with Pytest and Selenium <a name="selenium-tests"></a>

Running all tests is as simple as
```bash
run_pytest
```
  
## ITA Course <a name="ita"></a>

Find about each lab content [here](./docs/labs.md)

## References <a name="references"></a>

- [Steps followed to setup flask with mongodb][mongodb]
- [Autodoc modules][sphinx]
- [Directory structure explanation](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)

[mongodb]: https://flask-user.readthedocs.io/en/latest/mongodb_app.html
[sphinx]: https://www.sphinx-doc.org/en/master/
[pylint]: https://pylint.org/
[pytest]: https://docs.pytest.org/
