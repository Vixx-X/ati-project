from flask import render_template
from flask.views import View
# from flask_babel import gettext as _ # for i18n

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
