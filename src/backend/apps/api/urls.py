"""
Urls for media module/blueprint
"""

from . import api
from .views import user, post

api.add_resource(user.FriendView, "/users/<username>/friends")
api.add_resource(user.NotificationView, "/user/notifications/<notification>")
api.add_resource(post.PostView, '/api/posts')