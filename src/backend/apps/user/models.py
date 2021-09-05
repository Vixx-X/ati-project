"""
Models for User module
"""

from flask import current_app
from backend import db
from flask_user import UserMixin
from social_flask_mongoengine.models import FlaskStorage

from config import LANGUAGES  # for i18n
from flask_babel import gettext as _


class Config(db.Document):
    """
    Config and personalization for a user
    """

    PRIVACY_OPTIONS = (("PUBLIC", _("public")), ("PRIVATE", _("private")))
    privacy = db.StringField(max_length=10, choices=PRIVACY_OPTIONS)

    notify = db.BooleanField(default=True)

    THEME_OPTIONS = (("LIGHT", _("light mode")), ("DARK", _("dark mode")))
    theme = db.StringField(max_length=10, choices=THEME_OPTIONS)

    lang = db.StringField(max_length=3, choices=((a, b) for a, b in LANGUAGES.items()))

    @property
    def prefer_private(self):
        return self.privacy == "PRIVATE"


class User(db.Document, UserMixin):
    """
    User model for common user attributes and methods
    """

    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(max_length=128)
    email = db.EmailField(unique=True)
    email_confirmed_at = db.DateTimeField()
    password = db.StringField(max_length=255)

    # User information
    first_name = db.StringField(max_length=128, default="")
    last_name = db.StringField(max_length=128, default="")
    ci = db.IntField()

    birth_date = db.DateTimeField()
    GENDERS = (("F", _("femenine")), ("M", _("masculine")), ("O", _("other")))
    gender = db.StringField(max_length=1, choices=GENDERS)

    # Tokens
    twitter = db.StringField(default='')
    facebook = db.StringField(default='')

    # Relationships
    friends = db.SortedListField(
        db.ReferenceField("self", reverse_delete_url=db.CASCADE),
        default=[],
    )

    meta = {
        "collection": "users",
    }

    @property
    def social_auth(self):
        return FlaskStorage.user.objects(user=self)

    @property
    def is_active(self):
        return self.active

    @staticmethod
    def get_deleted_user():
        return User(first_name="[DELETED]")

    @classmethod
    def get_user_by_token(cls, token, expiration_in_seconds=None):
        # FIXING valid token on deleted user
        #
        # This function works in tandem with UserMixin.get_id()
        # Token signatures and timestamps are verified.
        # user_id and password_ends_with are decrypted.

        # Verifies a token and decrypts a User ID and parts of a User password hash
        user_manager = current_app.user_manager
        data_items = user_manager.verify_token(token, expiration_in_seconds)

        # Verify password_ends_with
        token_is_valid = False
        if data_items:

            # Load user by User ID
            user_id = data_items[0]
            password_ends_with = data_items[1]
            user = user_manager.db_manager.get_user_by_id(user_id)
            if not user: # <--- HERE
                return None
            user_password = '' if user_manager.USER_ENABLE_AUTH0 else user.password[-8:]

            # Make sure that last 8 characters of user password matches
            token_is_valid = user and user_password==password_ends_with

        return user if token_is_valid else None
