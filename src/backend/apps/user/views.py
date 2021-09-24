"""
Views for the user module.
"""

from backend.utils.views import TemplateView, FormView

# from flask_babel import gettext as _ # for i18n


class CheckEmailView(TemplateView):
    """
    CheckEmail view that notify user to check its email
    """

    template_name = "user/auth/check_email.html"


class ConfigView(FormView):
    """
    Config View to edit user configuration and personalization.
    """

    template_name = "user/configurations.html"


class NotificationView(TemplateView):
    """
    Notification View to alert or notify user of interactions or events.
    """

    template_name = "user/notifications.html"


class FriendView(TemplateView):
    """
    Friend View list of a User.
    """

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

    template_name = "user/search-page.html"


class ChatView(TemplateView):
    """
    Chat View
    """

    template_name = "user/chat.html"
