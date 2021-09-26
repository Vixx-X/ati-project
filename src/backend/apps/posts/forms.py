"""
Forms for posts app
"""

from flask_babel import lazy_gettext as _
from flask_wtf.form import FlaskForm
from wtforms import FieldList, StringField, validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import MultipleFileField, TextAreaField

from backend.apps.media.forms import FormMediaMixin


class PostForm(FlaskForm, FormMediaMixin):
    """
    Posts Form
    """

    title = StringField(
        _("Title"),
        validators=[
            validators.input_required(),
            validators.Length(max=255),
        ],
    )
    description = TextAreaField(
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
    media = MultipleFileField(_("Multimedia"))
    public = BooleanField(_("Public"))

    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        if not self.is_submitted():
            self.public.data = not user.prefer_private
