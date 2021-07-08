"""
Urls for showroom module/blueprint
"""

from flask_babel import gettext as _
from . import bp, views

list_of_rooms = [
    ("buttons", _("Buttons")),
    ("header", _("Header")),
    ("user_icon", _("User Icons")),
    ("card", _("Card")),
    ("header2", _("Header Main")),
    ("comments-users", _("Comments of Users")),
]

bp.add_url_rule("/", view_func=views.Index.as_view("index"))
bp.add_url_rule("/buttons/", view_func=views.Buttons.as_view("buttons"))
bp.add_url_rule("/header/", view_func=views.Header.as_view("header"))
bp.add_url_rule("/user-icon/", view_func=views.UserIcon.as_view("user_icon"))
bp.add_url_rule("/card/", view_func=views.Card.as_view("card"))
bp.add_url_rule("/header2/", view_func=views.Header2.as_view("header2"))
bp.add_url_rule("/comments-users/", view_func=views.Comments.as_view("comments-users"))