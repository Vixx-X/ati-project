"""
Views for the user module.
"""

from backend.utils.views import TemplateView

# from flask_babel import gettext as _ # for i18n


class CheckEmailView(TemplateView):
    """
    CheckEmail view that notify user to check its email
    """

    template_name = "user/auth/check_email.html"


class Config(TemplateView):
    """
    Config View to edit user configuration and personalization.
    """

    template_name = "user/configurations.html"


class Notification(TemplateView):
    """
    Notification View to alert or notify user of interactions or events.
    """

    template_name = "user/notifications.html"


class Friend(TemplateView):
    """
    Friend View list of a User.
    """

    template_name = "user/friend-list.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Profile(TemplateView):
    """
    Profile View
    """

    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class EditProfile(TemplateView):
    """
    Edit Profile View
    """

    template_name = "user/profile-edit.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Search(TemplateView):
    """
    Search View
    """

    template_name = "user/search-page.html"


class Description(TemplateView):
    """
    Edit Profile View
    """

    template_name = "user/profile-description.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Chat(TemplateView):
    """
    Chat View
    """

    template_name = "user/chat.html"
