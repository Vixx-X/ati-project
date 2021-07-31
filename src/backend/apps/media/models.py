"""
Models for Media module
"""

from re import T
from typing_extensions import Required
import mongoengine as db
from flask_babel import gettext as _
from mongoengine.fields import StringField
from abc import ABC

class Media(ABC, db.Document):
    """
    Base Media Class
    """
    meta = {
        'abstract': True
    }

    path = StringField(required = True)
    filename = StringField(required = True)
    format = StringField()
    width = StringField()
    heigth = StringField()

class Image(Media):
    """
    User model for common user attributes and methods
    """
    meta = {
        'collection': 'Image'
    }

    resolution = StringField()
    webp = StringField()
    png = StringField()

class Video(Media):
    """
    User model for common user attributes and methods
    """
    meta = {
        'collection': 'Video'
    }

    resolution = StringField()
    duration = StringField()

class Audio(Media):
    """
    User model for common user attributes and methods
    """
    meta = {
        'collection': 'Audio'
    }

    duration = StringField()

class Text(db.Document):
    """
    Model for Users' Texts publications
    """
    text = StringField(required = True)
