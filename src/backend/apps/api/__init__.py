"""
API module
"""

from flask import Blueprint
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES
from flask_babel import lazy_gettext as _  # for i18n

from backend.apps.api.utils import make_response


bp = Blueprint("api", __name__)


class ExtendedAPI(Api):
    """
    This class overrides 'handle_error' method of 'Api' class ,
    to extend global exception handing functionality of 'flask-restful'.
    """

    def handle_error(self, err):
        """
        It helps preventing writing unnecessary
        try/except block though out the application
        """
        print(err)  # log every exception raised in the application
        # Handle HTTPExceptions
        if isinstance(err, HTTPException):
            message = (
                getattr(
                    err,
                    "description",
                    HTTP_STATUS_CODES.get(err.code, ""),
                ),
            )
            return (
                make_response(message=message, status=err.code),
                err.code,
            )
        # If msg attribute is not set,
        # consider it as Python core exception and
        # hide sensitive error info from end user
        if not getattr(err, "message", None):
            return make_response(
                message=_("Server has encountered some error"), status=500
            )
        # Handle application specific custom exceptions
        return make_response(**err.kwargs, status=err.http_status_code)


api = ExtendedAPI(bp)

from . import urls
