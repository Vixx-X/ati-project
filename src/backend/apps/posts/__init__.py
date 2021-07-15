"""
Posts module for login behind posting
"""

from flask import Blueprint

bp = Blueprint("posts", __name__)

from . import urls
