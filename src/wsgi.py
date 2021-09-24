"""
Starting script for the flask app
"""
# Run a test server.

import os

from dotenv import load_dotenv
import click

from backend import init_app

ENV_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "env")
load_dotenv(os.path.join(ENV_DIR, ".env"))

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
    from loaddata import loaddata as ld

    return ld(filename, dry_run)


if __name__ == "__main__":
    app.run()
