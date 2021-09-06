"""
Place to register all blueprints
"""


def customize_social_auth():
    """
    Customize certain routes of social auth
    """
    from datetime import datetime

    from flask import Blueprint, current_app, g
    from flask_user import login_required, signals
    from social_core.actions import do_auth, do_complete, do_disconnect
    from social_flask.routes import do_login as base_do_login
    from social_flask.utils import psa

    social_auth = Blueprint("social", "social_flask")

    def do_login(backend, user, social_user):
        ret = base_do_login(backend=backend, user=user, social_user=social_user)
        # Set email_confirmed_at if not already set, is assuming that a
        # user only have one email, that is, the User is the UserMailClass
        if ret and not user.email_confirmed_at:
            user.email_confirmed_at = datetime.utcnow()
            user.save()

            # Send confirmed_email signal
            signals.user_confirmed_email.send(
                current_app._get_current_object(), user=user
            )

        return ret

    @social_auth.route("/sign-in/<string:backend>/", methods=("GET", "POST"))
    @psa("social.complete")
    def auth(backend):
        return do_auth(g.backend)

    @social_auth.route("/complete/<string:backend>/", methods=("GET", "POST"))
    @psa("social.complete")
    def complete(backend, *args, **kwargs):
        """Overrided view to auto confirm emails due to being confirmed by
        auth provider inside login"""

        return do_complete(g.backend, login=do_login, user=g.user, *args, **kwargs)

    @social_auth.route("/disconnect/<string:backend>/", methods=("POST",))
    @social_auth.route(
        "/disconnect/<string:backend>/<int:association_id>/", methods=("POST",)
    )
    @social_auth.route(
        "/disconnect/<string:backend>/<string:association_id>/", methods=("POST",)
    )
    @login_required
    @psa()
    def disconnect(backend, association_id=None):
        """Disconnects given backend from current logged in user."""
        return do_disconnect(g.backend, g.user, association_id)

    return social_auth


def register_blueprint(app):
    """
    Given an app register all blueprints for the application
    """
    from .apps import api, chat, media, posts, user

    # Register Blueprints
    app.register_blueprint(customize_social_auth(), uri_prefix="oauth")
    app.register_blueprint(api.bp, uri_prefix="/api")
    app.register_blueprint(chat.bp, url_prefix="/chat")
    app.register_blueprint(media.bp, url_prefix="/media")
    app.register_blueprint(posts.bp, url_prefix="/post")
    app.register_blueprint(user.bp, url_prefix="/user")

    if app.config["DEBUG"]:
        from .apps import showroom

        app.register_blueprint(showroom.bp, url_prefix="/showroom")
