"""
Utils functions for api module
"""


def _make_response(data=None, message=""):
    """
    Fotmat response
    """
    resp = {
        "message": str(message),
    }
    if data is None:
        resp["results"] = data
    return resp


def make_response(data=None, message="", status=200, **kwargs):
    """
    Make response resource from data
    """
    resp = {
        **_make_response(
            data=data,
            message=message,
        ),
        **kwargs,
    }
    return resp, status
