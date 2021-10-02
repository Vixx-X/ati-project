"""
Views for the posts module.
"""

from flask import abort, redirect
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

    def get_context_data(self, **kwargs):
        kwargs["create"] = self.object is None
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj and obj.author != self.user:
            abort(403)
        return obj

    def form_valid(self, form, *args, **kwargs):
        post = self.object or Post()
        form.populate_obj(obj=post)
        post.author = self.user
        post = post.save()
        return redirect(url_for("app.home", id=str(post.id)))
