"""
Urls for media module/blueprint
"""

from backend.apps.api.views import Post, Posts
from . import views
from backend import api

api.add_resource(Post, '/api/posts')
api.add_resource(Posts, '/api/posts/<int:page>')
