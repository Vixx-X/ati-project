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