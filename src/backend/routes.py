"""
Urls for the main app
"""

# routes
from flask import render_template
from flask.blueprints import Blueprint
from . import views

bp = Blueprint("app", __name__)

bp.add_url_rule("/", view_func=views.Home.as_view("home"))
bp.add_url_rule("/welcome/", view_func=views.LandingPage.as_view("landing"))
bp.add_url_rule("/login/", "login", views.Login, methods=["GET", "POST"])
bp.add_url_rule("/register/", view_func=views.Register.as_view("register"))
bp.add_url_rule("/forgotpassword/", view_func=views.ForgotPassword.as_view("forgotpassword"))

@bp.errorhandler(404)
def not_found(error):
    """
    Return 404 template if not found
    """
    return render_template("404.html"), 404
