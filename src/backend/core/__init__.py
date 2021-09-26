"""
Init for core app
"""

from flask import Blueprint, render_template, request, g, session
from flask_login import current_user

from backend import babel
from backend.core.urls import set_urls
from config import LANGUAGES, DEFAULT_LANGUAGE  # for i18n
from flask_babel import lazy_gettext as _  # for i18n


def init_app(app):
    """
    Initialize core app
    """

    bp = Blueprint("app", __name__)
    set_urls(app, bp)
    app.register_blueprint(bp)

    def render_error(error):
        return render_template(
            "error.html",
            error=error,
        )

    @app.errorhandler(404)
    def not_found(error):
        """
        Return 404 template if not found
        """
        return render_error(error), 404

    @app.errorhandler(500)
    def internal_error(error):
        """
        Return 500 template if internal error
        """
        return render_error(error), 500

    @app.before_request
    def global_user():
        g.user = current_user._get_current_object()  # pylint: disable=E0237

    # Make current user available on templates
    @app.context_processor
    def inject_theme():
        # if a user is logged in, use the theme from the user settings
        user = getattr(g, "user", None)
        if user is not None and user.is_active:
            return {"theme": "darkmode" if user.prefer_dark_mode else ""}

        # if we find session theme cookie, and its valid, then we use it
        session_theme = session.get("theme", None)
        if session_theme is not None:
            return {"theme": "darkmode" if session_theme == "darkmode" else ""}
        return {"theme": ""}

    # Make current user available on templates
    @app.context_processor
    def inject_user():
        try:
            return {"user": g.user}
        except AttributeError:
            return {"user": None}

    @babel.localeselector
    def get_locale():
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, "user", None)
        if user is not None and user.is_active:
            return user.prefer_lang or DEFAULT_LANGUAGE

        # if we find session lang cookie, and its valid, then we use it
        session_lang = session.get("lang", None)
        if session_lang and session_lang in LANGUAGES.keys():
            return session_lang

        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support es/en/pt in this
        # example.  The best match wins.
        return request.accept_languages.best_match(LANGUAGES.keys())
