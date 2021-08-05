"""
Views for the user module.
"""

from backend.utils.views import BaseView

# from flask_babel import gettext as _ # for i18n


class Config(BaseView):
    """
    Config View to edit user configuration and personalization.
    """

    template_name = "user/configurations.html"


class Notification(BaseView):
    """
    Notification View to alert or notify user of interactions or events.
    """

    template_name = "user/notifications.html"


class Friend(BaseView):
    """
    Friend View list of a User.
    """

    template_name = "user/friend-list.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Profile(BaseView):
    """
    Profile View
    """

    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class EditProfile(BaseView):
    """
    Edit Profile View
    """

    template_name = "user/profile-edit.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Search(BaseView):
    """
    Search View
    """

    template_name = "user/search-page.html"


class Description(BaseView):
    """
    Edit Profile View
    """

    template_name = "user/profile-description.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk", None)
        ctx = super().get_context_data()
        ctx["is_myuser"] = pk == 1
        return ctx


class Chat(BaseView):
    """
    Chat View
    """

    template_name = "user/chat.html"
