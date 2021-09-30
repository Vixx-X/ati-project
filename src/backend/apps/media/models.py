"""
Models for Media module
"""

from flask.helpers import url_for
import mongoengine as db

# from flask_babel import gettext as _
from mongoengine.fields import StringField
from pathlib import Path

from flask import send_from_directory

from backend.apps.media.utils import (
    get_media_root_path,
    get_media_upload_path,
    upload_file,
    upload_to,
)

from backend import thumb


class Media(db.Document):
    """
    Base Media Class
    """

    meta = {
        "allow_inheritance": True,
        "collection": "media",
    }

    upload_file = upload_file  # procedure to upload a file
    upload_to = upload_to  # upload path destiny
    get_media_root_path = get_media_root_path

    path = StringField(required=True)
    filename = StringField(required=True)
    format = StringField()
    width = StringField()
    heigth = StringField()

    static = False

    def __init__(self, file=None, static=False, **kwargs):
        """
        Magically get media data form fileStorege object
        """
        super().__init__(**kwargs)

        if file:
            self._file = file

        self.static = static

        if not self.path:
            self.path = get_media_upload_path(self)

    @property
    def data(self):
        """
        Return file data
        """
        if hasattr(self, "_file"):
            return self._file
        return send_from_directory(self.get_media_root_path(), str(self.path))

    @property
    def url(self):
        if self.static:
            return url_for("static", filename=self.path)
        return url_for("media.file", path=self.path)

    def save(self, **kwargs):
        """
        Save media and also upload file to server
        """
        self.upload_file()
        return super().save(**kwargs)

    def delete(self, **kwargs):
        """
        Delete media and also delete file on server
        """
        path = Path(self.upload_to())
        if path.is_file():
            try:
                path.unlink()
                for _ in range(2):
                    path = path.parent
                    if path.is_dir():
                        path.rmdir()
            except OSError:  # Not existent or directories with more media
                pass

        return super().delete(**kwargs)


class Image(Media):
    """
    Image media model
    """

    type = "image"

    resolution = StringField()

    def thumb(self, size, **kwargs):
        if self.static:
            return self.url
        thumb_url = thumb.get_thumbnail(self.path, size, **kwargs)
        if not thumb_url:
            return self.url
        if not thumb_url.startswith("/"):
            return f"/{thumb_url}"
        return thumb_url

    def as_dict(self):
        return self.to_mongo().to_dict()


class Audio(Media):
    """
    Audio media model
    """

    type = "audio"

    duration = StringField()


class Video(Media):
    """
    Video media model
    """

    type = "video"

    duration = StringField()
    resolution = StringField()
