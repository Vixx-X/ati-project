"""
Utils functions for api module
"""


from flask.json import jsonify


def _make_response(data=None, message=""):
    resp = {
        "message": str(message),
    }
    if data is None:
        resp["results"] = data
    return resp


def make_response(data=None, message="", status=200, **kwargs):
    resp = {
        **_make_response(
            data=data,
            message=message,
        ),
        **kwargs,
    }
    return resp, status
