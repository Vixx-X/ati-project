"""
Showroom module for showcase of components
"""

from flask import Blueprint

bp = Blueprint("showroom", __name__, template_folder="templates")

from . import urls
