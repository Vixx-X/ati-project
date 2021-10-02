"""
Forms for posts app
"""

from flask_babel import lazy_gettext as _
from flask_wtf.form import FlaskForm
from markupsafe import Markup
from wtforms import FieldList, StringField, validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import MultipleFileField, TextAreaField
from wtforms.widgets import CheckboxInput

from backend.apps.media.forms import FormMediaMixin


class LatchWidget(CheckboxInput):
    def __call__(self, field, **kwargs):
        inside = super().__call__(field, **kwargs)
        return Markup(
            '<label class="switch">%s<span class="slider round"></span></label>'
            % inside
        )


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
