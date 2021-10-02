"""
Api view that check for api health
"""

from flask_restful import Resource
from flask_wtf.csrf import generate_csrf

from backend.apps.api.utils import make_response as res


class Health(Resource):
    """
    Health entrypoint to account for api avaliabilty
    """

    def get(self):
        """
        Just return 200, and also csrf token for next request
        """
        csrf = generate_csrf()
        return res(data=str(csrf), message="Server started", status=200)
