"""
Urls for showroom module/blueprint
"""

from . import bp
from . import views

list_of_rooms = [
    ("botones", "Botones"),
    ("header", "Header"),
    ("user_icon", "Iconos de Usuario"),
    ("card", "Cart")
]

bp.add_url_rule("/", view_func=views.Index.as_view("index"))
bp.add_url_rule("/botones/", view_func=views.Botones.as_view("botones"))
bp.add_url_rule("/header/", view_func=views.Header.as_view("header"))
bp.add_url_rule("/user-icon/", view_func=views.UserIcon.as_view("user_icon"))
bp.add_url_rule("/card/", view_func=views.Card.as_view("card"))
