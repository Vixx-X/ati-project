"""
Views for comment module
"""

from backend.apps.api.views.utils import APIListView
from backend.apps.posts.models import Comment
from flask_babel import lazy_gettext as _  # for i18n

from backend.apps.posts.utils import get_comments_by_path, save_comment_by_path


class CommentListView(APIListView):
    resource = Comment

    def get_queryset(self):
        return get_comments_by_path(self.kwargs["path"])

    def post(self, data, **kwargs):
        """
        Create new comment
        """
        comment = self.resource(**data, author=self.user)
        save_comment_by_path(self.kwargs["path"], comment)

        return self.response(data=comment, status=201)
