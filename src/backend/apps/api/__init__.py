"""
Media module
"""

from flask import Blueprint

bp = Blueprint("api", __name__)

from . import urls
