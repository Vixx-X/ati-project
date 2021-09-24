"""
API module
"""

from flask import Blueprint
from flask.json import jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES

from .errors import ApiExceptions

bp = Blueprint("api", __name__)


class ExtendedAPI(Api):
    """This class overrides 'handle_error' method of 'Api' class ,
    to extend global exception handing functionality of 'flask-restful'.
    """

    def handle_error(self, err):
        """It helps preventing writing unnecessary
        try/except block though out the application
        """
        print(err)  # log every exception raised in the application
        # Handle HTTPExceptions
        if isinstance(err, HTTPException) or isinstance(err, ApiExceptions):
            return (
                jsonify(
                    {
                        "message": getattr(
                            err,
                            "description",
                            HTTP_STATUS_CODES.get(err.code, ""),
                        ),
                    }
                ),
                err.code,
            )
        # If msg attribute is not set,
        # consider it as Python core exception and
        # hide sensitive error info from end user
        if not getattr(err, "message", None):
            return jsonify({"message": "Server has encountered some error"}), 500
        # Handle application specific custom exceptions
        return jsonify(**err.kwargs), err.http_status_code


api = ExtendedAPI(bp)

from . import urls
