"""
Media module
"""

from flask import Blueprint

bp = Blueprint("chat", __name__)

from . import urls
