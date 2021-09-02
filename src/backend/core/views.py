"""
Views for the core app.
"""

from flask_login.utils import login_user
from backend.core.forms import LoginForm
from backend.utils.views import TemplateView
from flask import render_template, request, url_for, redirect, abort
from flask_login import current_user, login_required

# from flask_babel import gettext as _ # for i18n



class Home(TemplateView):
    """
    Home of the application.
    """

    decorators = [login_required]
    template_name = "home.html"


class LandingPage(TemplateView):
    """
    Landing page for unauthtenticated clients.
    """

    template_name = "landing-page.html"


class Register(TemplateView):
    """
    Register View.
    """

    template_name = "register.html"


class ForgotPassword(TemplateView):
    """
    ForgotPassword View.
    """

    template_name = "forgotpassword.html"
