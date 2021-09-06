"""
Forms for posts app
"""

from flask_babel import lazy_gettext as _
from flask_wtf.form import FlaskForm
from wtforms import FieldList, StringField, validators
from wtforms.fields.core import BooleanField

from backend.loading import get_class

Post = get_class("posts.models", "Post")


class PostForm(FlaskForm):
    """
    Posts Form
    """

    title = StringField(
        _("Title"),
        validators=[validators.input_required(), validators.Length(max=255)],
    )
    description = StringField(
        _("Description"),
        validators=[
            validators.Length(max=65536),
        ],
    )
    tags = FieldList(
        StringField(
            _("Tag"),
            validators=[
                validators.Length(max=255),
            ],
        )
    )
    public = BooleanField(_("Public"))

    def __init__(self, user, **kwargs):
        breakpoint()
        super().__init__(**kwargs)
