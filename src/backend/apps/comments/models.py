"""
Model for comments Module
"""

from backend import db
from backend.loading import get_class
from backend.apps.posts.models import Post

User = get_class("user.models", "User")

class Comment(db.Document):
    """
    Model for users` comments
    """

    author = db.ReferenceField(
        User, reverse_delete_rule=db.NULLIFY
    )
    post = db.ReferenceField(Post, reverse_delete_rule=db.NULLIFY)

    # Content
    content = db.StringField(max_length=65536)

    time_created = db.DateTimeField()

    def as_dict(self):
        raw = self.to_mongo().to_dict()
        raw["id"] = str(raw.pop("_id"))

        if "author" in raw:
            raw["author"] = self.author.as_dict()

        if "post" in raw:
            raw["post"] = self.post.as_dict()

        return raw
