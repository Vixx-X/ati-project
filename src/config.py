"""
Config file for the entire application
"""

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = os.getenv("DEBUG", "False").lower() in ["1", "t", "true"]

# MongoEngine Settings
# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
MONGODB_SETTINGS = {
    "db": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "27017")),
    "authentication_source": os.getenv("DB_AUTH_SOURCE", "admin"),
}

# Flask Mail settings
# https://flask-mail.readthedocs.io/en/latest/
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = os.getenv("MAIL_PORT", 587)
MAIL_USE_TLS = not DEBUG
MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")
MAIL_USERNAME = MAIL_DEFAULT_SENDER
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

# Flask User settings
# https://github.com/lingthio/Flask-User/blob/master/flask_user/user_manager__settings.py
USER_APP_NAME = "DEGVA"  # Shown in and email templates

# - E-mail settings
USER_EMAIL_SENDER_EMAIL = MAIL_DEFAULT_SENDER
USER_EMAIL_SENDER_NAME = "DEGVA"

# - Override templates
USER_LOGIN_TEMPLATE = "user/auth/login.html"
USER_FORGOT_PASSWORD_TEMPLATE = "user/auth/forgot-password.html"
USER_REGISTER_TEMPLATE = "user/auth/register.html"

USER_AFTER_LOGIN_ENDPOINT = "app.home"
USER_AFTER_LOGOUT_ENDPOINT = "app.welcome"
USER_AFTER_REGISTER_ENDPOINT = "user.edit"
USER_AFTER_FORGOT_PASSWORD_ENDPOINT = "user.check_email"


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Secret key for signing cookies
SECRET_KEY = os.getenv("SECRET_KEY", "secret")

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for signing the data.
CSRF_SESSION_KEY = SECRET_KEY + "_csrf"

# Static folder
STATIC_FOLDER = f"{BASE_DIR}/static/"

# Template folder
TEMPLATE_FOLDER = f"{BASE_DIR}/templates/"

# Template Auto Reload
TEMPLATES_AUTO_RELOAD = True

# Languages
# https://flask-babel.tkte.ch/
LANGUAGES = {
    "en": "english",
    "es": "español",
    "pt": "português",
}
BABEL_TRANSLATION_DIRECTORIES = f"{BASE_DIR}/translations/"

# Social Auth Config
# https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html
SOCIAL_AUTH_USER_MODEL = "backend.apps.user.models.User"
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ["keep"]
SOCIAL_AUTH_STORAGE = "social_flask_mongoengine.models.FlaskStorage"
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

SOCIAL_AUTH_SANITIZE_REDIRECTS = True  # sanitize possible open redirects
SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = True

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    "social_core.backends.facebook.FacebookOAuth2",
    # 'social_core.backends.twitter.TwitterOAuth',
)

# Facebook Backend
# https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html#oauth2
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("FACEBOOK_APP_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("FACEBOOK_APP_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
