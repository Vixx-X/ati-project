"""
Models for User module
"""

from flask import current_app, url_for
from flask_babel import gettext as _
from flask_user import UserMixin
from social_flask_mongoengine.models import FlaskStorage

from backend import db
from config import LANGUAGES as LANGS, DEFAULT_LANGUAGE  # for i18n

from backend.apps.media.models import Image

import re

NO_ASCII_REGEX = re.compile(r"[^\x00-\x7F]+")
NO_SPECIAL_REGEX = re.compile(r"[^\w._-]+", re.UNICODE)


def clean_username(value):
    """
    Cleaning username, could be expanded to deal with inappropriate
    words and stuff
    """
    value = NO_ASCII_REGEX.sub("", value)
    value = NO_SPECIAL_REGEX.sub("", value)
    return value


class Config(db.EmbeddedDocument):
    """
    Config and personalization for a user
    """

    PRIVACY_OPTIONS = (("PUBLIC", _("public")), ("PRIVATE", _("private")),)
    privacy = db.StringField(max_length=10, choices=PRIVACY_OPTIONS, default="PUBLIC",)

    notify = db.BooleanField(default=True)

    THEME_OPTIONS = (("LIGHT", _("light mode")), ("DARK", _("dark mode")),)
    theme = db.StringField(max_length=10, choices=THEME_OPTIONS, default="LIGHT",)

    LANGUAGES = [(a, b) for a, b in LANGS.items()]
    lang = db.StringField(max_length=3, choices=LANGUAGES, default=DEFAULT_LANGUAGE,)

    @property
    def prefer_private(self):
        """
        Get privacy preference of user
        """
        return self.privacy == "PRIVATE"


class User(db.Document, UserMixin):
    """
    User model for common user attributes and methods
    """

    active = db.BooleanField(default=True,)

    # User authentication information
    username = db.StringField(max_length=128,)
    email = db.EmailField(unique=True,)
    email_confirmed_at = db.DateTimeField()
    password = db.StringField(max_length=255,)

    # User information
    first_name = db.StringField(max_length=128, default="",)
    last_name = db.StringField(max_length=128, default="",)
    ci = db.IntField()

    # User media
    profile_photo = db.ReferenceField(Image,)
    banner_photo = db.ReferenceField(Image,)

    # User extra info
    description = db.StringField(max_length=255, default="",)
    birth_date = db.DateTimeField()
    GENDERS = [
        ("X", _("not specified")),
        ("F", _("femenine")),
        ("M", _("masculine")),
        ("O", _("other")),
    ]
    gender = db.StringField(max_length=1, choices=GENDERS,)
    colors = db.ListField(db.StringField(max_length=128), default=[],)
    books = db.ListField(db.StringField(max_length=128), default=[],)
    games = db.ListField(db.StringField(max_length=128), default=[],)
    langs = db.ListField(db.StringField(max_length=128), default=[],)
    music = db.ListField(db.StringField(max_length=128), default=[],)

    # Relationships
    friends = db.SortedListField(
        db.ReferenceField("self", reverse_delete_url=db.CASCADE,),
        default=[],
    )

    config = db.EmbeddedDocumentField(
        Config,
        reverse_delete_url=db.CASCADE,
        default=Config,
    )

    meta = {
        "collection": "users",
    }

    def get_profile_photo_url(self):
        if self.profile_photo:
            return self.profile_photo.url
        return url_for("static", filename="img/user/default_profile.jpg")

    def add_friend(self, friend):
        """
        Add a new friend
        """
        if friend not in self.friends and friend.id != self.id:
            self.friends.append(friend)

    def remove_friend(self, friend):
        """
        Remove a friend
        """
        self.friends.remove(friend)

    @property
    def social_auth(self):
        """
        Entrypoint to social_auth from my custom user
        """
        return FlaskStorage.user.objects(user=self)

    @property
    def is_active(self):
        """
        Return if user is active
        """
        return self.active

    @classmethod
    def get_deleted_user(cls):
        """
        Return a deleted username for templates
        """
        return User(username="[DELETED]")

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
            user_password = (
                "" if not user or user_manager.USER_ENABLE_AUTH0 else user.password[-8:]
            )  # <-- HERE

            # Make sure that last 8 characters of user password matches
            token_is_valid = user and user_password == password_ends_with

        return user if token_is_valid else None
