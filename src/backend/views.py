"""
Views for the core app.
"""

from backend.utils.views import BaseView

# from flask_babel import gettext as _ # for i18n


class Home(BaseView):
    """
    Home of the application.
    """

    template_name = "home.html"


class LandingPage(BaseView):
    """
    Landing page for unauthtenticated clients.
    """

    template_name = "landing-page.html"


class Login(BaseView):
    """
    Login View.
    """

    template_name = "login.html"


class Register(BaseView):
    """
    Register View.
    """

    template_name = "register.html"

class ForgotPassword(BaseView):
    """
    ForgotPassword View.
    """

    template_name = "forgotpassword.html"

class CreatePublication(BaseView):
    """
    CreatePublication View.
    """

    template_name = "create-publication.html"