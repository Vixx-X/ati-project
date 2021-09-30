"""
Views for the media module.
"""

import json
from flask import session
from flask_user import current_user
from flask_socketio import emit, join_room, leave_room
from flask_user.decorators import login_required

from backend.utils.views import DetailView, TemplateMixin, TemplateView
from .models import Chat

# from flask_babel import gettext as _ # for i18n


from backend import socketio
from backend.apps.chat.models import Message

@socketio.on("connect")
def connect():
    """
    Connecting user to pull of online users
    """
    room = session.get("room")
    join_room(room)

    if room == "UNIVERSE":
        emit("user_connected", {"username":current_user.username}, room=room)


@socketio.on("message")
def messages(message):
    """
    Get messages send by client and sent it to all in room
    """
    room = session.get("room")

    data = json.loads(message)

    # Save message to db
    msg = Message(content= data["message"], author=current_user)
    chat = Chat.objects.get_or_404(pk=room)
    chat.add_message(msg)
    chat.save()

    emit("message", {"message":msg.content, "time":msg.time_created}, room=room)


@socketio.on("disconnect")
def disconnect():
    """
    Left room
    """
    room = session.get("room")
    leave_room(room)

    if room == "UNIVERSE":
        emit("user_disconnected", {"username":current_user.username}, room=room)


class ChatView(DetailView):
    """
    Chat View
    """

    model = Chat

    decorators = [login_required]

    template_name = "chat/chat.html"


class ChatListView(TemplateView):
    """
    Chat list
    """

    template_name = "chat/chat.html"


