"""
Place to register all blueprints
"""

def register_blueprint(app):
    """
    Given an app register all blueprints for the application
    """
    from .apps import api, chat, media, posts, user
    from social_flask.routes import social_auth

    # Register Blueprints
    app.register_blueprint(social_auth)
    app.register_blueprint(api.bp, uri_prefix="/api")
    app.register_blueprint(chat.bp, url_prefix="/chat")
    app.register_blueprint(media.bp, url_prefix="/media")
    app.register_blueprint(posts.bp, url_prefix="/post")
    app.register_blueprint(user.bp, url_prefix="/user")

    if app.config["DEBUG"]:
        from .apps import showroom
        app.register_blueprint(showroom.bp, url_prefix="/showroom")
