"""
Media module
"""

from flask import Blueprint

bp = Blueprint("media", __name__)

from . import urls
