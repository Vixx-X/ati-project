"""
Views for the posts module.
"""

from flask import redirect
from flask.helpers import url_for

from backend.apps.posts.forms import PostForm
from backend.apps.posts.models import Post
from backend.utils.views import DetailView, UpdateView

# from flask_babel import gettext as _ # for i18n


class PostView(DetailView):
    """
    Post View to see the detail of a post and its comments.
    """

    template_name = "posts/post.html"
    model = Post
    object_name = "post"


class CreateUpdatePostView(UpdateView):
    """
    Create/Update View to the Post model.
    """

    template_name = "posts/post-update.html"
    form_class = PostForm
    model = Post

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form, *args, **kwargs):
        post = self.object or Post()
        form.populate_obj(obj=post)
        post = post.save()
        return redirect(url_for("posts.post-detail", id=str(post.id)))
