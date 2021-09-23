"""
Views for the core app.
"""

from flask_user import login_required

from backend.utils.views import TemplateView

# from flask_babel import gettext as _ # for i18n


class Home(TemplateView):
    """
    Home of the application.
    """

    decorators = [login_required]
    template_name = "home.html"


class LandingPage(TemplateView):
    """
    Landing page for unauthenticated clients.
    """

    template_name = "landing-page.html"
