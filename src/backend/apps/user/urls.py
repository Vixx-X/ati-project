"""
Urls for user module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/config/", view_func=views.Config.as_view("config"))
bp.add_url_rule("/notifications/", view_func=views.Notification.as_view("notification"))
bp.add_url_rule("/<int:pk>/", view_func=views.Profile.as_view("profile"))
bp.add_url_rule("/profile/", view_func=views.EditProfile.as_view("edit"))
bp.add_url_rule("/<int:pk>/friends/", view_func=views.Friend.as_view("friend"))
bp.add_url_rule(
    "/<int:pk>/description/", view_func=views.Description.as_view("description")
)
bp.add_url_rule("/search/", view_func=views.Search.as_view("search"))
bp.add_url_rule("/chat/", view_func=views.Chat.as_view("chat"))
bp.add_url_rule("/check_email/", view_func=views.CheckEmailView.as_view("check_email"))
