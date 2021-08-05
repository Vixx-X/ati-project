"""
Views for the posts module.
"""

from backend.apps.posts.forms import PostForm
from backend.utils.views import TemplateView, FormView
from flask_login import current_user

# from flask_babel import gettext as _ # for i18n


class Post(TemplateView):
    """
    Post View to see the detail of a post and its comments.
    """

    template_name = "posts/post.html"


class Comment(TemplateView):
    """
    Comment View to watch a comment in detail.
    """

    template_name = "user/comment.html"


class CreateUpdatePost(FormView):
    """
    Create/Update View to the Post model.
    """

    template_name = "posts/post-update.html"
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = current_user
        return kwargs
