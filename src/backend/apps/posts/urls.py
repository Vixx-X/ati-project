"""
Urls for posts module/blueprint
"""

from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/post/<int:id>/", view_func=views.Post.as_view("post"))
bp.add_url_rule("/comment/<int:id>/", view_func=views.Comment.as_view("comment"))
