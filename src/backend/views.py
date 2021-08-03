"""
Views for the core app.
"""

from flask_login.utils import login_user
from backend.forms import LoginForm
from backend.utils.views import BaseView
from flask import render_template, request, url_for, redirect, abort
from flask_user import current_user
from urllib.parse import urlparse, urljoin

# from flask_babel import gettext as _ # for i18n


def is_safe_url(target):
    """
    Check if a url is safe to redirect to
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and ref_url.netloc == test_url.netloc


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


def Login():
    """
    Login View
    """

    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(current_user)

        url = request.args.get("next")
        # is_safe_url should check if the url is safe for redirects.
        if not is_safe_url(url):
            return abort(400)

        return redirect(url or url_for("app.home"))

    return render_template("login.html", form=form)


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
