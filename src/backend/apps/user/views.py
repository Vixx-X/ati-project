"""
Views for the user module.
"""

from backend.utils.views import BaseView

# from flask_babel import gettext as _ # for i18n


class Config(BaseView):
    """
    Config View to edit user configuration and personalization.
    """

    template_name = "showroom/index.html"

    def get_context_data(self):
        """
        Place the list_of_rooms in the context
        """

        return {}


class Notification(BaseView):
    """
    Notification View to alert or notify user of interactions or events.
    """

    template_name = "showroom/buttons.html"


class Friend(BaseView):
    """
    Friend View list of a User.
    """

    template_name = "showroom/buttons.html"
