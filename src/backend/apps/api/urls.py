"""
Urls for media module/blueprint
"""

from . import api
from .views import user, post, comments

api.add_resource(user.FriendView, "/users/<username>/friends")
api.add_resource(user.NotificationView, "/user/notifications/<notification>")
api.add_resource(post.PostView, '/posts')
api.add_resource(comments.CommentView, '/posts/<string:postID>/comments')