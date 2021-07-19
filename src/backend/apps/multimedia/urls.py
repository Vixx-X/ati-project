"""
Urls for multimedia module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/media/", view_func=views.Media.as_view("media"))
