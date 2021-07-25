"""
Urls for user module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/config/", view_func=views.Config.as_view("config"))
bp.add_url_rule("/notifications/", view_func=views.Notification.as_view("notification"))
bp.add_url_rule("/<int:pk>/", view_func=views.Profile.as_view("profile"))
bp.add_url_rule("/<int:pk>/edit/", view_func=views.EditProfile.as_view("edit-profile"))
bp.add_url_rule("/<int:pk>/friends/", view_func=views.Friend.as_view("friend"))
