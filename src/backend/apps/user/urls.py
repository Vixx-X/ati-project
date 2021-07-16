"""
Urls for user module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/config/", view_func=views.Config.as_view("config"))
bp.add_url_rule("/notifications/", view_func=views.Notification.as_view("notification"))
bp.add_url_rule("/<int:id>/friends/", view_func=views.Friend.as_view("friend"))
