import datetime
import posixpath
from flask import request
from pathlib import Path
from flask import current_app
from werkzeug.utils import secure_filename


class BadConfigured(Exception):
    pass


class UnknownMedia(Exception):
    pass


def get_media_root_path(self=None):
    """
    Get media root path (self is given for customization)
    """
    return current_app.config["MEDIA_FOLDER"]


def get_media_upload_path(instance):
    """
    Get custom upload path to minimize collisions
    """
    class_name = instance.type.lower()
    filename = instance.filename
    return posixpath.join(
        class_name, datetime.datetime.now().strftime("%Y/%m"), filename
    )


def get_media_class(file):
    """
    Get the media class according to its MIME
    """

    from backend.apps.media.models import Image, Audio, Video

    media_map = {
        "image": Image,
        "audio": Audio,
        "video": Video,
    }

    media = current_app.config["ALLOWED_EXTENSIONS"]
    filename = secure_filename(file.filename)
    if not ("." in filename):
        raise UnknownMedia(f"{filename} is not a valid media or have no extension")

    for typ, exts in media.items():
        if filename.rsplit(".", 1)[1].lower() in exts:
            return media_map[typ]

    raise UnknownMedia(f"{filename} is not a valid media")


def save_media(file):
    """
    Save any kind of media depending of MIME
    """
    mediaClass = get_media_class(file)
    media = mediaClass(file=file, filename=secure_filename(file.filename))
    media.save()
    return media


def save_media_from_form(field_name):
    """
    Given a file name save media from form
    """
    if field_name not in request.files:
        raise BadConfigured(f"Request did not come with {field_name}")
    file = request.files[field_name]
    if file.filename:
        return save_media(file)
    return None


def create_or_replace(instance, file):
    """
    Create or replace any kind of media depending of MIME
    """
    if instance:
        instance.delete()
    return save_media(file)


def create_or_replace_from_form(instance, field_name):
    """
    Given a file name save or replace media from form
    """
    if field_name not in request.files:
        raise BadConfigured(f"Request did not come with {field_name}")
    file = request.files[field_name]
    if file.filename:
        return create_or_replace(instance, file)
    return None


def upload_to(instance):
    """
    Get upload to path from instance
    """
    root = instance.get_media_root_path()
    if instance.path and root:
        dst = posixpath.join(root, instance.path)
        return dst
    raise BadConfigured(
        "make sure MEDIA_FOLDER is correct and the instance have a path"
    )


def upload_file(instance):
    """
    Upload a fileStorege object on its media instance path
    """
    dst = instance.upload_to()
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    return instance.data.save(dst)
