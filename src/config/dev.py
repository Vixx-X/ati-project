"""
Config file for development
"""

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Define the database - we are working with
# # SQLite for this example
# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")
# DATABASE_CONNECT_OPTIONS = {}

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
    'en': 'English',
    'es': 'Español',
    'pt': 'português',
}
BABEL_TRANSLATION_DIRECTORIES = f"{BASE_DIR}/translations/"

# Template Auto Reload
TEMPLATES_AUTO_RELOAD = True



