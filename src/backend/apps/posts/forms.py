"""
Forms for posts app
"""

from flask_babel import lazy_gettext as _
from flask_wtf.form import FlaskForm
from wtforms import FieldList, StringField, validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import MultipleFileField, TextAreaField

from backend.apps.media.forms import FormMediaMixin
from backend.apps.user.forms import LatchWidget


class PostForm(FormMediaMixin, FlaskForm):
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
    public = BooleanField(
        _("Public"),
        widget=LatchWidget(),
    )

    def __init__(self, user, **kwargs):
        obj = kwargs.get("obj")
        super().__init__(**kwargs)
        if not self.is_submitted():
            self.public.data = obj.public if obj else not user.prefer_private
