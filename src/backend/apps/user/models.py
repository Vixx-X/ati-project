"""
Models for User module
"""

import re
from datetime import datetime

from flask import current_app
from flask.helpers import url_for
from flask_babel import gettext as _
from flask_user import UserMixin
from mongoengine.queryset.visitor import Q
from social_flask_mongoengine.models import FlaskStorage

from backend import db
from backend.apps.media.models import Image
from config.config import DEFAULT_LANGUAGE
from config.config import LANGUAGES as LANGS

NO_ASCII_REGEX = re.compile(r"[^\x00-\x7F]+")
NO_SPECIAL_REGEX = re.compile(r"[^\w_-]+", re.UNICODE)


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

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PRIVACY_OPTIONS = (
        (PUBLIC, _("public")),
        (PRIVATE, _("private")),
    )
    account_privacy = db.StringField(
        max_length=10,
        choices=PRIVACY_OPTIONS,
        default=PUBLIC,
    )

    notify = db.BooleanField(default=True)

    accept_friend_requests = db.BooleanField(default=True)

    LIGHT = "LIGHT"
    DARK = "DARK"
    THEME_OPTIONS = (
        (LIGHT, _("light mode")),
        (DARK, _("dark mode")),
    )
    theme = db.StringField(
        max_length=10,
        choices=THEME_OPTIONS,
        default=LIGHT,
    )

    LANGUAGES = list(LANGS.items())
    lang = db.StringField(
        max_length=3,
        choices=LANGUAGES,
        default=DEFAULT_LANGUAGE,
    )

    @property
    def prefer_private(self):
        """
        Get privacy preference of user
        """
        return self.account_privacy == self.PRIVATE

    @property
    def prefer_dark_mode(self):
        """
        Get theme preference of user
        """
        return self.theme == self.DARK

    @property
    def prefer_lang(self):
        """
        Get lang preference of user
        """
        return self.lang


class User(db.Document, UserMixin):
    """
    User model for common user attributes and methods
    """

    active = db.BooleanField(
        default=True,
    )

    # User authentication information
    username = db.StringField(
        max_length=128,
    )
    email = db.EmailField(
        unique=True,
    )
    email_confirmed_at = db.DateTimeField()
    password = db.StringField(
        max_length=255,
    )

    # User information
    first_name = db.StringField(
        max_length=128,
        default="",
    )
    last_name = db.StringField(
        max_length=128,
        default="",
    )
    ci = db.IntField()

    # User media
    profile_photo = db.ReferenceField(
        Image,
    )
    banner_photo = db.ReferenceField(
        Image,
    )

    # User extra info
    description = db.StringField(
        max_length=1024,
        default="",
    )
    birth_date = db.DateTimeField()
    GENDERS = [
        ("X", _("not specified")),
        ("F", _("femenine")),
        ("M", _("masculine")),
        ("O", _("other")),
    ]
    gender = db.StringField(
        max_length=1,
        choices=GENDERS,
    )
    colors = db.ListField(
        db.StringField(max_length=128),
        default=[],
    )
    books = db.ListField(
        db.StringField(max_length=128),
        default=[],
    )
    games = db.ListField(
        db.StringField(max_length=128),
        default=[],
    )
    langs = db.ListField(
        db.StringField(max_length=128),
        default=[],
    )
    music = db.ListField(
        db.StringField(max_length=128),
        default=[],
    )

    # Relationships
    friends = db.SortedListField(
        db.ReferenceField(
            "self",
            reverse_delete_url=db.CASCADE,
        ),
        ordering="username",
    )

    config = db.EmbeddedDocumentField(
        Config,
        reverse_delete_url=db.CASCADE,
        default=Config,
    )

    meta = {
        "collection": "users",
    }

    @property
    def chats(self):
        """
        Return user's chat
        """
        from backend.apps.chat.models import Chat

        return Chat.objects.filter(Q(user1=self) | Q(user2=self))

    @property
    def full_name(self):
        """
        Return user's fullname
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def prefer_private(self):
        """
        Get privacy preference of user
        """
        return self.config.prefer_private

    @property
    def prefer_dark_mode(self):
        """
        Get theme preference of user
        """
        return self.config.prefer_dark_mode

    @property
    def prefer_lang(self):
        """
        Get lang preference of user
        """
        return self.config.prefer_lang

    @property
    def posts(self):
        """
        Return user's posts
        """
        from backend.apps.posts.models import Post

        return Post.objects.filter(author=self)

    def as_dict(self):
        """
        Return user's info as dictionary
        """
        raw = self.to_mongo().to_dict()
        raw["id"] = str(raw.pop("_id"))

        if "banner_photo" in raw:
            raw["banner_photo"] = list(map(lambda x: x.as_dict(), self.banner_photo))

        if "profile_photo" in raw:
            raw["profile_photo"] = list(map(lambda x: x.as_dict(), self.profile_photo))

        if "email_confirmed_at" in raw:
            raw["email_confirmed_at"] = raw["email_confirmed_at"].isoformat()

        if "birth_date" in raw:
            raw["birth_date"] = raw["birth_date"].isoformat()

        if "friends" in raw:
            raw["friends"] = list(
                map(
                    lambda x: {
                        "username": x.username,
                        "photo": x.get_profile_photo_url,
                        "id": x.id,
                    },
                    self.friends,
                )
            )

        return raw

    def get_profile_photo_url(self):
        """
        Return user's profile photo url
        """
        return self.get_profile_photo.url

    @property
    def profile_photo_url(self):
        """
        Return user's profile photo url as property
        """
        return self.get_profile_photo_url()

    @property
    def get_profile_photo(self):
        """
        Return user's profile photo
        """
        if self.profile_photo:
            return self.profile_photo
        return Image(static=True, path="img/user/default-profile.png")

    def get_banner_url(self):
        """
        Return user's banner photo url
        """
        return self.get_profile_banner.url

    @property
    def banner_url(self):
        """
        Return user's banner photo url as property
        """
        return self.get_banner_url()

    @property
    def get_profile_banner(self):
        """
        Return user's banner photo
        """
        if self.banner_photo:
            return self.banner_photo
        return Image(static=True, path="img/user/default-banner.jpg")

    def is_friend(self, user):
        """
        Check is user is friend with current user
        """
        return user in self.friends

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
    def accept_friend_requests(self):
        """
        Return user's friend request preference
        """
        return self.config.accept_friend_requests

    @property
    def have_notification(self):
        """
        Return if user have notifications or not
        """
        return len(self.notifications)

    @property
    def notifications(self):
        """
        Return user's notifications
        """
        return Notification.objects.filter(receiver=self)

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
        return User(username="[DELETED]", first_name="[USER", last_name="DELETED]")

    @classmethod
    def get_user_by_token(cls, token, expiration_in_seconds=None):
        """
        Fixing Flask User bug
        """
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


class Notification(db.Document):
    """
    Notifications model
    """

    FRIEND_REQUEST_ACCEPTED = "FRA"
    FRIEND_REQUEST = "FR"
    CHECK_MESSAGE = "CM"
    CHECK_RESPONSE = "CR"
    CHECK_POST = "CP"
    PAGE = "P"
    TYPES = [
        (FRIEND_REQUEST, _("friend request")),
        (FRIEND_REQUEST_ACCEPTED, _("friend request accepted")),
        (CHECK_MESSAGE, _("check message")),
        (CHECK_POST, _("check post")),
        (CHECK_RESPONSE, _("check response")),
        (PAGE, _("page")),
    ]
    type = db.StringField(
        max_length=3,
        choices=TYPES,
    )

    receiver = db.ReferenceField(
        User,
        reverse_delete_url=db.CASCADE,
    )

    sender = db.ReferenceField(
        User,
        reverse_delete_url=db.CASCADE,
    )

    date_created = db.DateTimeField()

    def save(self, **kwargs):  # pylint: disable=W0221
        """
        Save notification model
        """
        if not self.pk:
            self.date_created = datetime.now()
        return super().save(**kwargs)

    map_title = {
        FRIEND_REQUEST: _("friend request"),
        FRIEND_REQUEST_ACCEPTED: _("friend request accepted"),
        CHECK_MESSAGE: _("check message"),
        CHECK_POST: _("check post"),
        PAGE: _("page"),
    }

    @property
    def title(self):
        """
        Return notification title
        """
        text = self.map_title.get(self.type, _("Notification Title"))
        num = text.count("%s")
        if not num or num > 1:
            return text

        return text % self.receiver.username

    map_message = {
        FRIEND_REQUEST: _("friend request message"),
        FRIEND_REQUEST_ACCEPTED: _("You and %s are now friends."),
        CHECK_MESSAGE: _("check message message"),
        CHECK_POST: _("check post message"),
        PAGE: _("page message"),
    }

    def url(self):
        """
        Return notification endpoint
        """
        return url_for("api.notification-list", id=str(self.pk))

    @property
    def message(self):
        """
        Return notification message
        """
        text = self.map_message.get(self.type, _("Notification Body"))
        num = text.count("%s")
        if not num or num > 1:
            return text

        return text % self.receiver.username

    def is_friend_request(self):
        """
        Check is notification is friend request
        """
        return self.receiver and self.sender and self.type == self.FRIEND_REQUEST
