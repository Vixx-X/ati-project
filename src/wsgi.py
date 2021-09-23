"""
Starting script for the flask app
"""
# Run a test server.

import os

from dotenv import load_dotenv

from backend import init_app

ENV_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/env/"
load_dotenv(ENV_DIR + ".env")

app = init_app()

if __name__ == "__main__":
    from sys import argv

    host, port = "0.0.0.0", 8080

    if len(argv) > 2:
        port = int(argv[2])
    if len(argv) > 1:
        host = argv[1]

    DEBUG = os.getenv("DEBUG", "False").lower() in ["1", "t", "true"]

    app.run(host=host, port=port, debug=DEBUG)
