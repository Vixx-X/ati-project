"""
Showroom module for showcase of components
"""

from flask import Blueprint

bp = Blueprint("user", __name__)

from . import urls
