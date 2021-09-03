"""
Urls for the main app
"""

from . import views


def set_urls(app, bp):
    bp.add_url_rule("/", view_func=views.Home.as_view("home"))
    bp.add_url_rule("/welcome/", view_func=views.LandingPage.as_view("landing"))
