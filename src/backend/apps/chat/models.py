"""
Models for Media module
"""

from datetime import datetime

from backend import db
from backend.apps.user.models import User
from backend.apps.posts.models import get_time

# from flask_babel import gettext as _


class Message(db.EmbeddedDocument):
    """
    Base Messages class
    """

    author = db.ReferenceField(User)

    # Content
    content = db.StringField(max_length=65536)

    time_created = db.DateTimeField()

    @property
    def time(self):
        return get_time(self.time_created)

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        self.time_created = datetime.utcnow()


class Chat(db.Document):
    """
    User model for common user attributes and methods
    """

    user1 = db.ReferenceField(
        User,
        reverse_delete_rule=db.CASCADE,
    )
    user2 = db.ReferenceField(
        User,
        reverse_delete_rule=db.CASCADE,
    )

    messages = db.EmbeddedDocumentListField(Message, default=[])

    def add_message(self, msg):
        self.messages.append(msg)

    def get_other_user(self, user):
        return self.user1 if user == self.user2 else self.user2

    def last_msg(self):
        return self.messages[-1].content

    meta = {
        "collection": "chats",
    }
