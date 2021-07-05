from flask.helpers import url_for
from flask.views import View
from flask import render_template

class BaseView(View):
    template_name = None

    def get_template_name(self):
        if self.template_name is None:
            raise NotImplementedError()
        return self.template_name

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def get_context_data(self):
        return {}

    def dispatch_request(self):
        return self.render_template(self.get_context_data())


class Index(BaseView):
    template_name = "showroom/index.html"

    def get_context_data(self):
        from .urls import list_of_rooms
        urls = { tag:url_for(f'showroom.{name}') for name, tag in list_of_rooms }
        return {"list": urls}


class Botones(BaseView):
    template_name = "showroom/botones.html"


class Header(BaseView):
    template_name = "showroom/header.html"


class UserIcon(BaseView):
    template_name = "showroom/user-icon.html"

