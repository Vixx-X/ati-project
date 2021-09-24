"""
Main app factory to boostrap the application
"""

from flask import Flask
from flask_restful import Api
from flask_babel import Babel
from flask_mongoengine import MongoEngine
from flask_wtf.csrf import CSRFProtect
from social_flask_mongoengine.models import init_social
from werkzeug.middleware.proxy_fix import ProxyFix
from backend.apps.user.user_manager import UserManager

from backend.blueprints import register_blueprint

api = Api()
db = MongoEngine()
babel = Babel()
user_manager = UserManager()
csrf = CSRFProtect()


def init_app(config_file="config"):
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

    # Initialize Plugins
    import backend.apps.api.urls
    api.init_app(app)
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

    from backend.apps.user.models import User

    user_manager.init_app(app, db, User)
    
    with app.app_context():
        # Include our Routes, and the core app
        from backend import core

        core.init_app(app)

        register_blueprint(app)

        return app
