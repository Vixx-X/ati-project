"""
Forms for user app
"""
from flask.helpers import url_for
from flask_babel import lazy_gettext as _
from flask_user.forms import ChangePasswordForm as BaseChangePasswordForm
from flask_user.forms import ChangeUsernameForm as BaseChangeUsernameForm
from flask_user.forms import EditUserProfileForm
from flask_user.forms import ForgotPasswordForm as BaseForgotPasswordForm
from flask_user.forms import LoginForm as BaseLoginForm
from flask_user.forms import RegisterForm as BaseRegisterForm
from flask_user.forms import (
    ResendEmailConfirmationForm as BaseResendEmailConfirmationForm,
)
from flask_user.forms import ResetPasswordForm as BaseResetPasswordForm
from flask_user.forms import (
    password_validator,
    unique_email_validator,
    unique_username_validator,
    username_validator,
)
from flask_wtf.form import FlaskForm  # for i18n
from wtforms import (
    BooleanField,
    DateField,
    FileField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    validators,
)
from wtforms.fields.core import FieldList, RadioField
from wtforms.fields.simple import HiddenField, TextAreaField
from wtforms.widgets import CheckboxInput, ListWidget, html_params
from wtforms.widgets.html5 import DateInput
from markupsafe import Markup

from backend.apps.media.forms import FormMediaMixin

from .models import Config, User

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


class CalendarWidget(DateInput):
    """
    Calendar Widget
    """

    def __call__(self, field, **kwargs):
        inside = super().__call__(field, **kwargs)
        return Markup("%s" % inside)


class CustomInfoWidget(ListWidget):
    """
    Custom widget for profile info cards
    """

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = ["<div {}>".format(html_params(**{"class": "long-card"}))]
        html.append(
            f"{field.label(**{'class' : 'label-card black'})}<div class='content-inputs'>"
        )
        for index, subfield in enumerate(field):
            if self.prefix_label:
                html.append(
                    f"<div class='input-content'>{subfield()}<button type='button'><img id='element{index}' class='delete-content' loading='lazy' src={url_for('static', filename='img/icons/delete.svg')} alt='Delete detail' /></button> {subfield.label(**{'class' : 'd-none'})}</div>"
                )
            else:
                html.append(
                    f"<div class='input-content'>{subfield()}<button type='button'><img id='element{index}' class='delete-content' loading='lazy' src={url_for('static', filename='img/icons/delete.svg')} alt='Delete detail' /></button> {subfield.label(**{'class' : 'd-none'})}</div>"
                )
        html.append(
            f"</div><button class='morecontent'><img loading='lazy' src={url_for('static', filename='img/icons/plus-sign.svg')} alt='Add publication'></button></div>"
        )
        return Markup("".join(html))


class ProfileForm(FormMediaMixin, EditUserProfileForm):
    """
    User Profile Form
    """

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

    description = TextAreaField(_("Description"))
    birth_date = DateField(
        _("Birth Day"),
        widget=CalendarWidget(),
    )
    gender = SelectField(_("Gender"), choices=User.GENDERS)

    colors = FieldList(StringField(_("Favorite Colors")), widget=CustomInfoWidget())

    books = FieldList(StringField(_("Favorite Books")), widget=CustomInfoWidget())

    games = FieldList(StringField(_("Favorite Video Games")), widget=CustomInfoWidget())
    langs = FieldList(
        StringField(_("Favorite Programming Languages")), widget=CustomInfoWidget()
    )
    music = FieldList(StringField(_("Favorite Music")), widget=CustomInfoWidget())

    submit = SubmitField(_("Update"))


class LatchWidget(CheckboxInput):
    """
    Latch widget
    """

    def __call__(self, field, **kwargs):
        inside = super().__call__(field, **kwargs)
        return Markup(
            '<label class="switch">%s<span class="slider round"></span></label>'
            % inside
        )


class CustomListWidget(ListWidget):
    """
    List input widget for users interest
    """

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = [
            "<div {}>".format(html_params(**{"class": "container-personalization"}))
        ]
        for subfield in field:
            if self.prefix_label:
                html.append(
                    f"<div class='radio-button d-flex jc-space_between'>{subfield.label(**{'class' : 'black'})} {subfield()}</div>"
                )
            else:
                html.append(
                    f"<div class='radio-button d-flex jc-space_between'>{subfield()} {subfield.label(**{'class' : 'black'})}</div>"
                )
        html.append("</div>")
        return Markup("".join(html))


class ConfigForm(FlaskForm):
    """
    User Configuration form
    """

    account_privacy = BooleanField(
        _("Private Account"),
        widget=LatchWidget(),
    )

    notify = BooleanField(
        _("Notify via email"),
        widget=LatchWidget(),
    )

    accept_friend_requests = BooleanField(
        _("Accept friend requests"),
        widget=LatchWidget(),
    )

    theme = RadioField(
        _("Themes"),
        choices=Config.THEME_OPTIONS,
        widget=CustomListWidget(),
    )

    lang = SelectField(
        _("Languages"),
        choices=Config.LANGUAGES,
    )

    def __init__(self, **kwargs):
        obj = kwargs.get("obj", None)
        super().__init__(**kwargs)
        if not self.is_submitted() and obj:
            self.account_privacy.data = obj.prefer_private

    def populate_obj(self, obj):
        """
        Save forms data on obj
        """
        super().populate_obj(obj)
        obj.account_privacy = (
            Config.PRIVATE if self.account_privacy.data else Config.PUBLIC
        )
