"""
Views for the posts module.
"""

from flask import redirect
from flask.helpers import url_for

from backend.apps.posts.forms import PostForm
from backend.utils.views import TemplateView, FormView
from flask_login import current_user
from backend.loading import get_class

# from flask_babel import gettext as _ # for i18n
Post = get_class("posts.models", "Post")
User = get_class("user.models", "User")


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
    model = Post

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(id=current_user.id)
        kwargs["user"] = user
        return kwargs

    def form_valid(self, form, *args, **kwargs):
        post = self.object or Post()

        post.title = form.title

        post.save()
        return redirect(url_for("post.post-detail", id=post._id))

