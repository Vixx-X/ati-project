"""
Models for User module
"""

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
