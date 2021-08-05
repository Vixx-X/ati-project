"""
Main app factory to boostrap the application
"""

from flask import Flask, request, session
from flask_login.login_manager import LoginManager
from flask_mongoengine import MongoEngine
from flask_babel import Babel
from flask_user.user_manager import UserManager
from flask_wtf.csrf import CSRFProtect

db = MongoEngine()
babel = Babel()
login = LoginManager()
csrf = CSRFProtect()


def init_app(config_file=None):
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)

    if not config_file:
        config_file = "config.dev"

    app.config.from_object(f"{config_file}")
    static_folder = app.config["STATIC_FOLDER"]
    if static_folder:
        app.static_folder = static_folder

    template_folder = app.config["TEMPLATE_FOLDER"]
    if template_folder:
        app.template_folder = template_folder

    # Initialize Plugins
    db.init_app(app) # db

    try:
        mongo_client = db.get_connection()
        mongo_client.admin.command('ismaster')
    except Exception:
        host = app.config["MONGODB_SETTINGS"]["host"]
        port = app.config["MONGODB_SETTINGS"]["port"]
        raise Exception(f'Could not connect to MongoDB, Are you sure is running on {host}:{port}?')


    babel.init_app(app) # i18n
    login.init_app(app) # login
    csrf.init_app(app) # csrf tokens

    from backend.apps.user.models import User

    user_manager = UserManager(app, db, User)  # pylint: disable=W0612

    with app.app_context():
        # Include our Routes
        from . import routes

        from .apps import api, chat, media, posts, user, showroom

        # Register Blueprints
        app.register_blueprint(routes.bp)
        app.register_blueprint(showroom.bp, url_prefix="/showroom")
        app.register_blueprint(api.bp, uri_prefix="/api")
        app.register_blueprint(chat.bp, url_prefix="/chat")
        app.register_blueprint(media.bp, url_prefix="/media")
        app.register_blueprint(posts.bp, url_prefix="/post")
        app.register_blueprint(user.bp, url_prefix="/user")

        login.login_view = "user:login"

        @babel.localeselector
        def get_locale():
            if request.args.get("lang"):
                session["lang"] = request.args.get("lang")
            return session.get("lang", "en")

        return app
