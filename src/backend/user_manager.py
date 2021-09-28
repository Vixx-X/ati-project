"""
Override Custom User Manager and components for flask-user
"""

from flask_user import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    """
    Wrapper custom for flask_user UserManager
    """

    def __init__(self, **kwargs):
        if len(kwargs):
            super().__init__(**kwargs)

    def init_app(
        self,
        app,
        db,
    ):
        from backend.apps.user.models import User

        UserClass = User
        self.app = app
        return super().init_app(
            app,
            db,
            UserClass,
        )

    def customize(self, app):
        """
        Configuring custom forms
        """
        from backend.apps.user import forms

        self.ChangePasswordFormClass = forms.ChangePasswordForm
        self.ChangeUsernameFormClass = forms.ChangeUsernameForm
        self.EditUserProfileFormClass = forms.ProfileForm
        self.ForgotPasswordFormClass = forms.ForgotPasswordForm
        self.LoginFormClass = forms.LoginForm
        self.RegisterFormClass = forms.RegisterForm
        self.ResendEmailConfirmationFormClass = forms.ResendEmailConfirmationForm
        self.ResetPasswordFormClass = forms.ResetPasswordForm
