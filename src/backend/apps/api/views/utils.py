"""
Views for the api module.
"""

from flask_restful import Resource

from flask_user import current_user


class APIView(Resource):
    """
    Base api view to get self.user as current user
    """

    def dispatch_request(self, *args, **kwargs):
        self.user = current_user._get_current_object()  # current user
        return super().dispatch_request(*args, **kwargs)
