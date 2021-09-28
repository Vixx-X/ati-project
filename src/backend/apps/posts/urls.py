"""
Urls for posts module/blueprint
"""

# from flask_babel import gettext as _
from . import bp, views

bp.add_url_rule(
    "",
    view_func=views.CreateUpdatePostView.as_view("post-create"),
)

bp.add_url_rule(
    "/<string:id>",
    view_func=views.PostView.as_view("post-detail"),
)

bp.add_url_rule(
    "/<string:id>/edit",
    view_func=views.CreateUpdatePostView.as_view("post-edit"),
)
