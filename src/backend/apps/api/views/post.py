"""
Views for the media module.
"""

from backend.apps.api.views.utils import APIDetailView, APIListView
from backend.apps.posts.models import Post


class PostListView(APIListView):
    resource = Post

    def get_resource_filter(self):
        return {"public": True}

    def get_resource_kwargs(self, data):
        return {"author": self.user, **data}


class PostDetailView(APIDetailView):
    resource = Post
