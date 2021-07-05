"""
Urls for the main app
"""

# routes
from flask import render_template
from flask.blueprints import Blueprint

bp = Blueprint("app", __name__)


@bp.errorhandler(404)
def not_found(error):
    """
    Return 404 template if not found
    """
    return render_template("404.html"), 404
