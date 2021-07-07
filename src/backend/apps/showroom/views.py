"""
Views for the showroom module.
"""

from flask import render_template
from flask.helpers import url_for
from flask.views import View


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


class Botones(BaseView):
    """
    Showcase for button component.
    """

    template_name = "showroom/botones.html"


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
