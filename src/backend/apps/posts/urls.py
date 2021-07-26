"""
Urls for posts module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule("/<int:id>/", view_func=views.Post.as_view("post"))
bp.add_url_rule("/comment/<int:id>/", view_func=views.Comment.as_view("comment"))
bp.add_url_rule("/createpublication/", view_func=views.CreatePublication.as_view("createpublication"))
bp.add_url_rule("/modifypublication/", view_func=views.ModifyPublication.as_view("modifypublication"))