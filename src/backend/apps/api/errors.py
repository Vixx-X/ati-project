"""
Custom API Error Exceptions
"""


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


class UnauthorizedError(ApiExceptions):
    """Unauthorized exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(http_status_code=401, *args, **kwargs)


class ResourceNotFoundError(ApiExceptions):
    """Resource not found exception"""