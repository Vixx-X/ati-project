"""
Urls for media module/blueprint
"""
from flask import send_from_directory

from backend.apps.media.utils import get_media_root_path
from . import bp


@bp.route("/<path:path>")
def file(path):
    return send_from_directory(get_media_root_path(), path)
