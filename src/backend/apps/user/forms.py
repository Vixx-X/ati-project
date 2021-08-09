"""
Forms for user app
"""

from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from flask_babel import lazy_gettext as _ # for i18n

# Forms

class LoginForm(FlaskForm):
    """
    Login Form
    """

    username = StringField(
        _("Username or email"),
        validators=[
            validators.input_required(),
        ],
    )
    password = PasswordField(
        _("Password"),
        validators=[
            validators.input_required(),
            validators.Length(min=8),
        ],
    )


class RegisterForm(FlaskForm):
    """
    Register Form
    """

    username = StringField(
        _("Username"),
        validators=[
            validators.input_required(),
        ],
    )
    email = StringField(
        _("Email"),
        validators=[
            validators.input_required(),
        ],
    )
    password = PasswordField(
        _("Password"),
        validators=[
            validators.input_required(),
            validators.Length(min=8),
        ],
    )
    password2 = PasswordField(
        _("Re type password"),
        validators=[
            validators.input_required(),
            validators.Length(min=8),
        ],
    )
