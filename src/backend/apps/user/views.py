"""
Views for the user module.
"""

from flask import session, sessions, url_for
from flask_user import login_required

from backend.apps.user.forms import ConfigForm
from backend.utils.views import TemplateView, UpdateView

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


class FriendView(TemplateView):
    """
    Friend View list of a User.
    """

    decorators = [login_required]

    template_name = "user/friend-list.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class ProfileView(TemplateView):
    """
    Profile View
    """

    decorators = [login_required]
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class SearchView(TemplateView):
    """
    Search View
    """

    decorators = [login_required]

    template_name = "user/search-page.html"


class ChatView(TemplateView):
    """
    Chat View
    """

    decorators = [login_required]

    template_name = "user/chat.html"
