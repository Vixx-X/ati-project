"""
Init for core app
"""

from flask import Blueprint, render_template, request, session
from flask.globals import g
from flask_login import current_user

from backend import babel
from backend.core.urls import set_urls


def init_app(app):
    """
    Initialize core app
    """

    bp = Blueprint("app", __name__)
    set_urls(app, bp)
    app.register_blueprint(bp)

    @app.errorhandler(404)
    def not_found(error):
        """
        Return 404 template if not found
        """
        return render_template("404.html", error=error), 404

    @app.before_request
    def global_user():
        g.user = current_user._get_current_object()  # pylint: disable=E0237

    # Make current user available on templates
    @app.context_processor
    def inject_user():
        try:
            return {"user": g.user}
        except AttributeError:
            return {"user": None}

    @babel.localeselector
    def get_locale():
        if request.args.get("lang"):
            session["lang"] = request.args.get("lang")
        return session.get("lang", "en")
