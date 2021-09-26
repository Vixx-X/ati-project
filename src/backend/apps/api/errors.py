"""
Custom API Error Exceptions
"""

from flask_babel import lazy_gettext as _

class ApiExceptions(Exception):
    """Base class for api exceptions"""

    def __init__(self, http_status_code: int, *args, **kwargs):
        # If the key `msg` is provided, provide the msg string
        # to Exception class in order to display
        # the msg while raising the exception
        self.code = self.http_status_code = http_status_code
        self.kwargs = kwargs
        msg = kwargs.get("msg", kwargs.get("message"))
        self.description = msg
        if msg:
            args = (msg,)
            super().__init__(args)
        self.args = list(args)
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])


class ValidationError(ApiExceptions):
    """Should be raised in case of custom validations"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            http_status_code=400,
            message=_("One or more required fields are missing"), *args,
            **kwargs
        )


class NotUniqueError(ApiExceptions):
    """Should be raised in case of a element already exist"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            http_status_code=409, message=_("Already exist"), *args, **kwargs
        )


class UnauthorizedError(ApiExceptions):
    """Unauthorized exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            http_status_code=401, message=_("You are not authorized"), *args, **kwargs
        )


class ResourceNotFoundError(ApiExceptions):
    """Resource not found exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(http_status_code=404, message=_("Resource does not exist."), *args, **kwargs)
