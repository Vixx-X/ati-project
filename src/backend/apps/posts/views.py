"""
Views for the posts module.
"""

from backend.utils.views import BaseView

# from flask_babel import gettext as _ # for i18n


class Post(BaseView):
    """
    Post View to see the detail of a post and its comments.
    """

    template_name = "posts/post.html"

    def __init__(self) -> None:
        return


class Comment(BaseView):
    """
    Comment View to watch a comment in detail.
    """

    template_name = "user/comment.html"

    def __init__(self) -> None:
        return
