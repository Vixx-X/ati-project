"""
Urls for the main app
"""

# routes
from flask import render_template, request, session
from flask.blueprints import Blueprint
from flask.globals import g
from flask_login import login_manager
from backend.apps.user.models import User
from . import views
from . import babel
from . import login_manager

bp = Blueprint("app", __name__)

bp.add_url_rule("/", view_func=views.Home.as_view("home"))
bp.add_url_rule("/welcome/", view_func=views.LandingPage.as_view("landing"))
bp.add_url_rule("/login/", "login", views.Login, methods=["GET", "POST"])
bp.add_url_rule("/register/", view_func=views.Register.as_view("register"))
bp.add_url_rule(
    "/forgotpassword/", view_func=views.ForgotPassword.as_view("forgotpassword")
)


@login_manager.user_loader
def load_user(userid):
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass


@app.before_request
def global_user():
    g.user = login.current_user


# Make current user available on templates
@app.context_processor
def inject_user():
    try:
        return {"user": g.user}
    except AttributeError:
        return {"user": None}


@bp.errorhandler(404)
def not_found(error):
    """
    Return 404 template if not found
    """
    return render_template("404.html"), 404


@babel.localeselector
def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")
