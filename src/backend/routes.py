# routes
from flask import render_template
from flask.blueprints import Blueprint

bp = Blueprint("app", __name__)


@bp.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
