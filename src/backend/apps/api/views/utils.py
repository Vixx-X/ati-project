"""
Views for the api module.
"""

from flask_restful import Resource
from flask_user import current_user

from backend.apps.api.decorators import login_required


class APIView(Resource):
    """
    Base api view to get self.user as current user
    """
    decorators = [login_required]

    def dispatch_request(self, *args, **kwargs):
        self.user = current_user._get_current_object()  # current user
        return super().dispatch_request(*args, **kwargs)
