"""
Urls for media module/blueprint
"""

from . import api
from .views import comments, post, user

# user
api.add_resource(user.FriendView, "/users/<string:username>/friends", endpoint="friend-list")
api.add_resource(user.NotificationView, "/user/notifications/<string:id>", endpoint="notification-list")

# posts
api.add_resource(post.PostListView, "/posts", endpoint="post-list")
api.add_resource(post.PostDetailView, "/posts/<string:id>", endpoint="post-detail")
api.add_resource(comments.CommentListView, "/posts/<string:id>/comments<path:path>", endpoint="comments-list")
