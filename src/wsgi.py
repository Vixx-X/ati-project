"""
Starting script for the flask app
"""
# Run a test server.

import os

from dotenv import load_dotenv
import click

from backend import init_app

from loaddata import loaddata as ld

ENV_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/env/"
load_dotenv(ENV_DIR + ".env")

app = init_app()

@app.cli.command("loaddata")
@click.argument("filename", type=click.Path(exists=True))
@click.argument("dry_run", type=click.BOOL, required=False)
def loaddata(filename, dry_run=False):
    """
    Load fixture data on db:

    FILENAME (path) to give the root file of fixtures.

    DRY_RUN (bool) load data without saving it into the db.
    """
    return ld(filename, dry_run)


if __name__ == "__main__":
    from sys import argv

    host, port = "0.0.0.0", 8080

    if len(argv) > 2:
        port = int(argv[2])
    if len(argv) > 1:
        host = argv[1]

    DEBUG = os.getenv("DEBUG", "False").lower() in ["1", "t", "true"]

    app.run(host=host, port=port, debug=DEBUG)
