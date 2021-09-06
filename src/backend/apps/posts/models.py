"""
Models for User module
"""

# from flask_babel import lazy_gettext as _
from datetime import datetime

from backend import db
from backend.loading import get_class

User = get_class("user.models", "User")


class Post(db.Document):
    """
    Model for users` posts
    """

    author = db.ReferenceField(
        User, reverse_delete_rule=db.NULLIFY
    )  # hacer la referencia a user model

    # content
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=65536)
    tags = db.ListField(
        db.StringField(max_length=255),
        default=[],
    )

    # metadata
    public = db.BooleanField(default=True)

    time_created = db.DateTimeField()
    time_edited = db.DateTimeField()
    edited = db.BooleanField(default=False)

    meta = {
        "collection": "posts",
    }

    def get_author(self):
        """
        Get Author of post
        """
        if self.author:
            return self.author
        return User.get_deleted_user()

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
