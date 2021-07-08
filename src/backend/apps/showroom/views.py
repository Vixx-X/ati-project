"""
Views for the showroom module.
"""

from flask import render_template
from flask.helpers import url_for
from flask.views import View

from flask_babel import gettext as _

class BaseView(View):
    """
    Mixin View to shortcut basic functionalities.
    """

    template_name = None

    def get_template_name(self):
        """
        Return the template_name of class if it is set, raise NotImplementedError otherwise.
        """
        if self.template_name is None:
            raise NotImplementedError()
        return self.template_name

    def render_template(self, context):
        """
        Method to render template given a context
        """
        return render_template(self.get_template_name(), **context)

    def get_context_data(self): # pylint: disable=R0201
        """
        Stud method to get context data
        """
        return {}

    def dispatch_request(self):
        return self.render_template(self.get_context_data())


class Index(BaseView):
    """
    Index View to showcase all rooms.
    """

    template_name = "showroom/index.html"

    def get_context_data(self):
        """
        Place the list_of_rooms in the context
        """

        from .urls import list_of_rooms

        urls = {tag: url_for(f"showroom.{name}") for name, tag in list_of_rooms}
        return {"list": urls}


class Buttons(BaseView):
    """
    Showcase for button component.
    """

    template_name = "showroom/buttons.html"


class Header(BaseView):
    """
    Showcase for header component.
    """

    template_name = "showroom/header.html"


class UserIcon(BaseView):
    """
    Showcase for user-icon component.
    """

    template_name = "showroom/user-icon.html"


class Card(BaseView):
    """
    Showcase for card component.
    """

    template_name = "showroom/card.html"


class Header2(BaseView):
    """
    Showcase for header2 component.
    """

    template_name = "showroom/header2.html"

class Comments(BaseView):
    """
    Showcase for comments-users component.
    """

    template_name = "showroom/comments-users.html"


class Footers(BaseView):
    """
    Showcase for footer component.
    """

    template_name = "showroom/footer.html"


class Heading(BaseView):
    """
    Showcase for heading component.
    """

    template_name = "showroom/heading.html"


class LongCards(BaseView):
    """
    Showcase for long cards component.
    """

    template_name = "showroom/long-cards.html"

class Notification(BaseView):
    """
    Showcase for notification component.
    """

    template_name = "showroom/notification.html"


class SearchButton(BaseView):
    """
    Showcase for search component.
    """

    template_name = "showroom/search-button.html"


class Chat(BaseView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/chat.html"
