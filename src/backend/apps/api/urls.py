"""
Urls for media module/blueprint
"""

from . import api
from .views import comments, post, user

# user
api.add_resource(user.FriendView, "/users/<string:username>/friends")
api.add_resource(user.NotificationView, "/user/notifications/<string:id>")

# posts
api.add_resource(post.PostListView, "/posts")
api.add_resource(post.PostDetailView, "/posts/<string:id>")
api.add_resource(comments.CommentListView, "/posts/<string:id>/comments<path:path>")
