"""
Urls for media module/blueprint
"""

from . import bp, views

bp.add_url_rule("/image/", view_func=views.Image.as_view("image"))
bp.add_url_rule("/video/", view_func=views.Video.as_view("video"))
bp.add_url_rule("/audio/", view_func=views.Audio.as_view("audio"))
