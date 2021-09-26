"""
Utils functions for api module
"""


from flask.json import jsonify


def _make_response(data=None, message=""):
    resp = {
        "message": message,
    }
    if data:
        resp["results"] = data
    return resp


def make_response(data=None, message="", status=200, **kwargs):
    return (
        jsonify(
            {
                **_make_response(
                    data=data,
                    message=message,
                ),
                **kwargs,
            }
        ),
        status,
    )
