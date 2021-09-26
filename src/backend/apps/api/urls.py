"""
Urls for media module/blueprint
"""

from . import api
from .views import user, post, comments

# user
api.add_resource(user.FriendView, "/users/<username>/friends")
api.add_resource(user.NotificationView, "/user/notifications/<int:id>")

# posts
api.add_resource(post.PostListView, "/posts")
api.add_resource(post.PostDetailView, "/posts/<int:id>")
api.add_resource(comments.CommentListView, "/posts/<int:id>/comments<path:path>")
