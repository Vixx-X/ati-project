"""
Config file for development
"""

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Define the database - we are working with
# MongoDB for this example
MONGODB_SETTINGS = {
    "db": "project",
    "username": "admin",
    "password": "1234",
    "host": "localhost",
    "port": 27017,
}

# Flask User settings
# https://github.com/lingthio/Flask-User/blob/master/flask_user/user_manager__settings.py
USER_APP_NAME = "ATI Social"    # Shown in and email templates
USER_REQUIRE_RETYPE_PASSWORD = True    # Retype pass on register

# - E-mail settings
USER_ENABLE_USERNAME = True   # Enable username authentication
USER_ENABLE_EMAIL = True      # Enable email authentication
USER_EMAIL_SENDER_EMAIL = "noreply@ati.vittorioadesso.com"
USER_EMAIL_SENDER_NAME = "ATI"

# - Override templates
USER_LOGIN_TEMPLATE = "user/login.html"
USER_FORGOT_PASSWORD_TEMPLATE = "user/forgot-password.html"
USER_REGISTER_TEMPLATE = "user/register.html"

USER_AFTER_LOGIN_ENDPOINT = "home"
USER_AFTER_LOGOUT_ENDPOINT = "welcome"
USER_AFTER_REGISTER_ENDPOINT = "user.edit"
USER_AFTER_FORGOT_PASSWORD_ENDPOINT = "user.check_email"


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Static folder
STATIC_FOLDER = f"{BASE_DIR}/static/"

# Template folder
TEMPLATE_FOLDER = f"{BASE_DIR}/templates/"

# Languages
LANGUAGES = {
    "en": "english",
    "es": "español",
    "pt": "português",
}
BABEL_TRANSLATION_DIRECTORIES = f"{BASE_DIR}/translations/"

# Template Auto Reload
TEMPLATES_AUTO_RELOAD = True

# Social Auth Config
# https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html
SOCIAL_AUTH_USER_MODEL = "backend.apps.user.models.User"
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ["keep"]
SOCIAL_AUTH_STORAGE = "social_flask_mongoengine.models.FlaskStorage"
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = True

# Facebook Backend
# https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html#oauth2
SOCIAL_AUTH_FACEBOOK_KEY = "328893792274101"
SOCIAL_AUTH_FACEBOOK_SECRET = SECRET_KEY + "_fadebook"
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
