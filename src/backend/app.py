"""
Module for main app and root page
"""

import flask

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    """
    Route in root path to greet everyone
    """
    return "Hello World!\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # open for everyone
