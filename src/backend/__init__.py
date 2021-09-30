"""
Main app factory to boostrap the application
"""
from flask import Flask
from flask_babel import Babel
from flask_mongoengine import MongoEngine
from flask_wtf.csrf import CSRFProtect
from social_flask_mongoengine.models import init_social
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_thumbnails import Thumbnail

from backend.blueprints import register_blueprint
from backend.user_manager import UserManager

db = MongoEngine()
babel = Babel()
user_manager = UserManager()
csrf = CSRFProtect()
thumb = Thumbnail()


def init_app(config_file="config", testing=False):
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)

    # Reading configs
    app.config.from_object(f"{config_file}")

    # Default for static
    static_folder = app.config["STATIC_FOLDER"]
    if static_folder:
        app.static_folder = static_folder

    # Default for template
    template_folder = app.config["TEMPLATE_FOLDER"]
    if template_folder:
        app.template_folder = template_folder

    # Chill trailing slash check
    app.url_map.strict_slashes = False

    # Initialize Plugins
    if testing:
        app.config["MONGODB_SETTINGS"]["db"] = "testing_db"
    db.init_app(app)  # db

    try:
        # test connection
        mongo_client = db.get_connection()
        mongo_client.admin.command("ismaster")
    except Exception as e:
        host = app.config["MONGODB_SETTINGS"]["host"]
        port = app.config["MONGODB_SETTINGS"]["port"]
        raise Exception(
            f"Could not connect to MongoDB, Are you sure is running on {host}:{port}?"
        ) from e

    init_social(app, db)  # social auth
    babel.init_app(app)  # i18n
    csrf.init_app(app)  # csrf tokens
    thumb.init_app(app)  # thumbs

    user_manager.init_app(app, db)

    with app.app_context():
        # Include our Routes, and the core app
        from backend import core

        core.init_app(app)

        register_blueprint(app)

        return app
