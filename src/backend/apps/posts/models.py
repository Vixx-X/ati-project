"""
Models for User module
"""

# from flask_babel import lazy_gettext as _
from datetime import datetime

from backend import db
from backend.apps.user.models import  User


class Post(db.Document):
    """
    Model for users` posts
    """

    author = db.ReferenceField(
        User, reverse_delete_rule=db.NULLIFY
    )

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

    def as_dict(self):
        raw = self.to_mongo().to_dict()
        raw["id"] = str(raw.pop("_id"))
        
        if "time_created" in raw:
            raw['time_created'] = raw['time_created'].isoformat()
        
        if "time_edited" in raw:
            raw['time_edited'] = raw['time_edited'].isoformat()

        if "author" in raw:
            raw["author"] = self.author.as_dict()

        return raw

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
