"""
Models for User module
"""

from backend import db
from flask_user import UserMixin
from flask_babel import gettext as _ # for i18n

class User(db.Document, UserMixin):
    active = db.BooleanField(default=True)

    # User authentication information
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    # User information
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')

    # Tokens
    twitter = db.StringField(default='')
    facebook = db.StringField(default='')

    # Birth
    birth_date = db.DateTimeField()
    GENDERS = (('F',_('femenine')), ('M',_('masculine')), ('O',_('other')))
    gender = db.StringField(max_lenhth=1, choices=GENDERS)

    # Relationships
    friends = db.SortedListField(db.EmbeddedDocumentField("User"), default=[])

