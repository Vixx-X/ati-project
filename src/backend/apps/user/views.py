"""
Views for the user module.
"""

from flask import session, url_for
from flask_user import login_required

from backend.apps.user.forms import ConfigForm
from backend.apps.user.utils import get_common_friends, get_common_friends_number, get_user_friends, search_users
from backend.utils.views import DetailView, TemplateView, UpdateView
from backend.apps.user.models import User

# from flask_babel import gettext as _ # for i18n


class CheckEmailView(TemplateView):
    """
    CheckEmail view that notify user to check its email
    """

    template_name = "user/auth/check_email.html"


class ConfigView(UpdateView):
    """
    Config View to edit user configuration and personalization.
    """

    decorators = [login_required]

    template_name = "user/configurations.html"
    form_class = ConfigForm

    def get_object(self, *args, **kwargs):
        return self.user.config

    def get_success_url(self):
        self.user.save()
        session["theme"] = "darkmode" if self.user.prefer_dark_mode else ""
        session["lang"] = self.user.prefer_lang
        return url_for("user.config")


class NotificationView(TemplateView):
    """
    Notification View to alert or notify user of interactions or events.
    """

    decorators = [login_required]

    template_name = "user/notifications.html"


class FriendView(DetailView):
    """
    Friend View list of a User.
    """

    decorators = [login_required]
    template_name = "user/friend-list.html"
    model = User
    model_pk = pk_or_slug_url = "username"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        target_user = self.object or self.user
        ctx["friends"] = get_user_friends(target_user, self.user)
        for friend in ctx["friends"]:
            setattr(friend, "common_friends", get_common_friends_number(friend, self.user))

        return ctx


class ProfileView(DetailView):
    """
    Profile View
    """

    decorators = [login_required]
    template_name = "user/profile.html"
    model = User
    model_pk = pk_or_slug_url = "username"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx["target_user"] = self.object or self.user
        return ctx


class SearchView(TemplateView):
    """
    Search View
    """

    decorators = [login_required]

    template_name = "user/search-page.html"

    def get_context_data(self, **kwargs):
        term = self.args.get("term","")
        ctx = super().get_context_data(**kwargs)
        ctx["users"] = search_users(term)
        for friend in ctx["users"]:
            setattr(friend, "common_friends", get_common_friends_number(friend, self.user))
        ctx["term"] = term
        return ctx


class ChatView(TemplateView):
    """
    Chat View
    """

    decorators = [login_required]

    template_name = "user/chat.html"
