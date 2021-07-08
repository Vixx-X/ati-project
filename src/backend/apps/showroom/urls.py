"""
Urls for showroom module/blueprint
"""

from flask_babel import gettext as _
from . import bp, views

list_of_rooms = [
    ("buttons", _("Buttons")),
    ("header", _("Header")),
    ("user_icon", _("User Icons")),
    ("card", _("Cart")),
]

bp.add_url_rule("/", view_func=views.Index.as_view("index"))
bp.add_url_rule("/buttons/", view_func=views.Buttons.as_view("buttons"))
bp.add_url_rule("/header/", view_func=views.Header.as_view("header"))
bp.add_url_rule("/user-icon/", view_func=views.UserIcon.as_view("user_icon"))
bp.add_url_rule("/card/", view_func=views.Card.as_view("card"))
