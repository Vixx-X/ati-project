"""
Models for User module
"""

from flask_babel import lazy_gettext as _, format_datetime as _d
from datetime import datetime, timedelta

from backend import db
from backend.apps.media.models import Media
from backend.apps.user.models import User

from flask_user import current_user


def get_time(time):
    now = datetime.now()
    delta = time - now
    if delta < timedelta(seconds=30):
        return _("Less than 30 seconds ago")
    if delta < timedelta(minutes=5):
        return _("Less than 5 minutes ago")
    if delta < timedelta(minutes=10):
        return _("Less than 10 minutes ago")
    if delta < timedelta(days=2):
        return _("Today")
    if delta < timedelta(days=2):
        return _("Yesterday")
    return _d(time, format="%A %d-%m-%Y, %H:%M")


class Comment(db.EmbeddedDocument):
    """
    Model for users` comments
    """

    _id = db.ObjectIdField(required=True, default=lambda: db.ObjectId())

    author = db.ReferenceField(User)

    # Content
    content = db.StringField(max_length=65536)

    # response
    comments = db.EmbeddedDocumentListField(
        "self",
        default=[],
    )

    time_created = db.DateTimeField()

    @property
    def get_author(self):
        """
        Get Author of post
        """
        if self.author:
            return self.author
        return User.get_deleted_user()

    @property
    def time(self):
        return get_time(self.time_created)

    @property
    def get_firts_comments(self):
        return self.comments[:3]

    def as_dict(self):
        raw = self.to_mongo().to_dict()
        raw["id"] = str(raw.pop("_id"))

        if "time_created" in raw:
            raw["time_created"] = raw["time_created"].isoformat()
        if "author" in raw:
            raw["author"] = self.author.as_dict()

        return raw


class Post(db.Document):
    """
    Model for users` posts
    """

    author = db.ReferenceField(User, reverse_delete_rule=db.NULLIFY)

    # content
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=65536)
    tags = db.ListField(
        db.StringField(max_length=255),
        default=[],
    )

    media = db.ListField(
        db.ReferenceField(
            Media,
            reverse_delete_rule=db.CASCADE,
        ),
    )

    # metadata
    public = db.BooleanField(default=True)

    time_created = db.DateTimeField()
    time_edited = db.DateTimeField()
    edited = db.BooleanField(default=False)

    comments = db.EmbeddedDocumentListField(
        Comment,
        default=[],
    )

    meta = {
        "collection": "posts",
    }

    @property
    def primary_media(self):
        if self.media:
            return self.media[0]
        return None

    @property
    def all_media(self):
        if self.media:
            return self.media
        return None
    
    @property
    def time(self):
        return get_time(self.time_created)

    def as_dict(self):
        raw = self.to_mongo().to_dict()
        raw["id"] = str(raw.pop("_id"))

        if "time_created" in raw:
            raw["time_created"] = get_time(raw["time_created"])

        if "time_edited" in raw:
            raw["time_edited"] = get_time(raw["time_edited"])

        if "author" in raw:
            raw["author"] = self.author.as_dict()

        return raw

    @property
    def get_author(self):
        """
        Get Author of post
        """
        if self.author:
            return self.author
        return User.get_deleted_user()

    @property
    def is_my_post(self):
        return current_user == self.author

    def save(self, *args, **kwargs):
        """
        Override return method to update created or updated time
        """
        if not self.time_created:
            self.time_created = datetime.now()
        else:
            self.time_edited = datetime.now()
            self.edited = True
        return super().save(*args, **kwargs)
