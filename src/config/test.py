"""
Config file for the testing the application
"""

# Define the application directory
import os

from .config import *

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = os.getenv("DEBUG", "False").lower() in ["1", "t", "true"]

# MongoEngine Settings
# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
MONGODB_SETTINGS = {
    "db": os.getenv("DB_NAME", "test"),
    "username": os.getenv("DB_USERNAME", "admin"),
    "password": os.getenv("DB_PASSWORD", "1234"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "27017")),
    "authentication_source": os.getenv("DB_AUTH_SOURCE", "admin"),
}

# Flask Mail settings
# https://flask-mail.readthedocs.io/en/latest/
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
MAIL_USE_TLS = True
MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME", "test@test.com")
MAIL_USERNAME = MAIL_DEFAULT_SENDER
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "test")

# - E-mail settings
USER_EMAIL_SENDER_EMAIL = MAIL_DEFAULT_SENDER
