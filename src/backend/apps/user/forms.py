"""
Forms for user app
"""

from flask_babel import lazy_gettext as _  # for i18n
from wtforms import (
    PasswordField,
    StringField,
    validators,
    BooleanField,
    SubmitField,
    FileField,
    DateField,
    SelectField,
)
from flask_user.forms import (
    LoginForm as BaseLoginForm,
    RegisterForm as BaseRegisterForm,
    ChangePasswordForm as BaseChangePasswordForm,
    ChangeUsernameForm as BaseChangeUsernameForm,
    ForgotPasswordForm as BaseForgotPasswordForm,
    ResetPasswordForm as BaseResetPasswordForm,
    ResendEmailConfirmationForm as BaseResendEmailConfirmationForm,
    EditUserProfileForm,
    password_validator,
    username_validator,
    unique_email_validator,
    unique_username_validator,
)

from wtforms.fields.simple import HiddenField
from backend.apps.media.forms import FormMediaMixin
from .models import User


# Forms


class ChangePasswordForm(BaseChangePasswordForm):
    """
    Change Password Form
    """

    old_password = PasswordField(
        _("Old Password"),
        validators=[
            validators.DataRequired(_("Old Password is required")),
        ],
    )
    new_password = PasswordField(
        _("New Password"),
        validators=[
            validators.DataRequired(_("New Password is required")),
            password_validator,
        ],
    )
    retype_password = PasswordField(
        _("Retype New Password"),
        validators=[
            validators.EqualTo(
                "new_password",
                message=_("New Password and Retype Password did not match"),
            )
        ],
    )
    submit = SubmitField(_("Change password"))


class ChangeUsernameForm(BaseChangeUsernameForm):
    """Change username form."""

    new_username = StringField(
        _("New Username"),
        validators=[
            validators.DataRequired(_("Username is required")),
            username_validator,
            unique_username_validator,
        ],
    )
    old_password = PasswordField(
        _("Old Password"),
        validators=[
            validators.DataRequired(_("Old Password is required")),
        ],
    )
    submit = SubmitField(_("Change username"))


class LoginForm(BaseLoginForm):
    """
    Login Form
    """

    username = StringField(
        _("Username or email"),
        validators=[
            validators.DataRequired(_("Username or email is required")),
        ],
    )
    password = PasswordField(
        _("Password"),
        validators=[
            validators.DataRequired(_("Password is required")),
            validators.Length(min=8),
        ],
    )
    remember_me = BooleanField(_("Remember me"))
    submit = SubmitField(_("Sign in"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username.label.text = _("Username or Email")


class RegisterForm(BaseRegisterForm):
    """
    Register Form
    """

    username = StringField(
        _("Username"),
        validators=[
            validators.DataRequired(_("Username is required")),
            username_validator,
            unique_username_validator,
        ],
    )
    email = StringField(
        _("Email"),
        validators=[
            validators.DataRequired(_("Email is required")),
            validators.Email(_("Invalid Email")),
            unique_email_validator,
        ],
    )
    password = PasswordField(
        _("Password"),
        validators=[
            validators.DataRequired(_("Password is required")),
            password_validator,
        ],
    )
    retype_password = PasswordField(
        _("Re type password"),
        validators=[
            validators.EqualTo(
                "password",
                message=_(
                    "Password and Retype Password did not match",
                ),
            )
        ],
    )

    invite_token = HiddenField(_("Token"))

    submit = SubmitField(_("Register"))


class ForgotPasswordForm(BaseForgotPasswordForm):
    """Forgot password form."""

    email = StringField(
        _("Your email address"),
        validators=[
            validators.DataRequired(_("Email address is required")),
            validators.Email(_("Invalid Email address")),
        ],
    )
    submit = SubmitField(_("Send reset password email"))


class ResendEmailConfirmationForm(BaseResendEmailConfirmationForm):
    """Resend email confirmation form."""

    email = StringField(
        _("Your email address"),
        validators=[
            validators.DataRequired(_("Email address is required")),
            validators.Email(_("Invalid Email address")),
        ],
    )
    submit = SubmitField(_("Resend email confirmation email"))


class ResetPasswordForm(BaseResetPasswordForm):
    """Reset password form."""

    new_password = PasswordField(
        _("New Password"),
        validators=[
            validators.DataRequired(_("New Password is required")),
            password_validator,
        ],
    )
    retype_password = PasswordField(
        _("Retype New Password"),
        validators=[
            validators.EqualTo(
                "new_password",
                message=_("New Password and Retype Password did not match"),
            )
        ],
    )
    next = HiddenField()
    submit = SubmitField(_("Change password"))


class ProfileForm(FormMediaMixin, EditUserProfileForm):

    first_name = StringField(
        _("First name"),
        validators=[validators.DataRequired()],
    )
    last_name = StringField(
        _("Last name"),
        validators=[validators.DataRequired()],
    )

    profile_photo = FileField(_("Profile Photo"))

    banner_photo = FileField(_("Banner Photo"))

    birth_date = DateField(_("Birth Day"), format="%d-%m-%Y")

    gender = SelectField(_("Gender"), choices=User.GENDERS)

    submit = SubmitField(_("Update"))
