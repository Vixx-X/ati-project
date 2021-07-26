"""
Forms for core app
"""

from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField


class LoginForm(FlaskForm):
    """
    Login Form
    """
    username = StringField("Username", validators=[validators.input_required(),])
    password = PasswordField("Password", validators=[validators.input_required(), validators.Length(min=8),])

