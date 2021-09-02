"""
Urls for the main app
"""

from . import views


def set_urls(app, bp):
    bp.add_url_rule("/", view_func=views.Home.as_view("home"))
    bp.add_url_rule("/welcome/", view_func=views.LandingPage.as_view("landing"))
    bp.add_url_rule("/register/", view_func=views.Register.as_view("register"))
    bp.add_url_rule(
        "/forgotpassword/", view_func=views.ForgotPassword.as_view("forgotpassword")
    )
