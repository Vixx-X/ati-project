"""
Urls for chat module/blueprint
"""

from . import bp, views

bp.add_url_rule("/<string:pk>", view_func=views.ChatView.as_view("chat"))
bp.add_url_rule("/", view_func=views.ChatListView.as_view("chat-list"))
