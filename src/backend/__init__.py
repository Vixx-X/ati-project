"""
Main app factory to boostrap the application
"""

from flask import Flask, request, session
from flask_mongoengine import MongoEngine
from flask_babel import Babel
from flask_user.user_manager import UserManager
from backend.apps.user.models import User

db = MongoEngine()
babel = Babel()

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
    db.init_app(app)
    babel.init_app(app)
    user_manager = UserManager(app, db, User)

    with app.app_context():
        # Include our Routes
        from . import routes

        # from .apps import api, chat, multimedia, posts, user
        from .apps import showroom, user, posts

        # Register Blueprints
        app.register_blueprint(routes.bp)
        app.register_blueprint(showroom.bp, url_prefix="/showroom")
        # app.register_blueprint(api.bp)
        # app.register_blueprint(chat.bp)
        # app.register_blueprint(multimedia.bp)
        app.register_blueprint(posts.bp)
        app.register_blueprint(user.bp, url_prefix="/user")

        @babel.localeselector
        def get_locale():
            if request.args.get('lang'):
                session['lang'] = request.args.get('lang')
            return session.get('lang', 'en')

        return app
