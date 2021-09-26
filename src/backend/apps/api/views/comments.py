"""
Views for comment module
"""

from backend.apps.api import api
from backend.apps.api.views.utils import APIListView
from backend.apps.posts.models import Comment
from flask_babel import lazy_gettext as _  # for i18n

from backend.apps.posts.utils import get_comments_by_path, save_comment_by_path


class CommentListView(APIListView):
    resource = Comment

    def process_context(self):
        self.path = '/'.join([self.kwargs["id"], self.kwargs["path"]])
        return super().process_context()

    def get_queryset(self):
        ret = get_comments_by_path(self.path)
        for parent in ret["comments"]:
            for replies in parent["comment"]:
                # TODO agregar reply
                pk, *path = parent["more"]
                replies["reply"] = api.url_for(CommentListView, id=pk, path="/".join(path))
            if "more" in parent:
                pk, *path = parent["more"]
                parent["more"] = api.url_for(CommentListView, id=pk, path="/".join(path)) + f"?page={self.page+1}&size={self.size}"
            pk, *path = parent["more"]
            parent["reply"] = api.url_for(CommentListView, id=pk, path="/".join(path))
        if "more" in ret:
            pk, *path = ret["more"]
            ret["more"] = api.url_for(CommentListView, id=pk, path="/".join(path)) + f"?page={self.page+1}&size={self.size}"

        return ret

    def post(self, data, **kwargs):
        """
        Create new comment
        """
        comment = self.resource(**data, author=self.user)
        save_comment_by_path(self.path, comment)

        return self.response(data=comment, status=201)
