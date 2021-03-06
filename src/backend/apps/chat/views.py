"""
Views for the media module.
"""

import functools
import json

from flask import session
from flask_socketio import disconnect, emit, join_room, leave_room
from flask_user import current_user
from flask_user.decorators import login_required

from backend import socketio
from backend.apps.chat.models import Message
from backend.utils.views import DetailView, TemplateView

from .models import Chat


def authenticated_only(f):
    """
    Decorator that disconnect unauthenticated users
    """

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped


@socketio.on("connect")
@authenticated_only
def handle_connect():
    """
    Connecting user to pull of online users
    """
    room = session.get("room")
    join_room(room)

    if room == "UNIVERSE":
        emit("user_connected", {"username": current_user.username}, room=room)


@socketio.on("message")
@authenticated_only
def handle_messages(message):
    """
    Get messages send by client and sent it to all in room
    """
    room = session.get("room")

    data = json.loads(message)

    # Save message to db
    msg = Message(content=data["message"], author=current_user)
    chat = Chat.objects.get_or_404(pk=room)
    chat.add_message(msg)
    chat.save()

    emit(
        "message",
        {
            "content": msg.content,
            "time": str(msg.time),
            "author": str(current_user.pk),
        },
        room=room,
    )


@socketio.on("disconnect")
@authenticated_only
def handle_disconnect():
    """
    Left room
    """
    room = session.get("room")
    leave_room(room)

    if room == "UNIVERSE":
        emit("user_disconnected", {"username": current_user.username}, room=room)


class ChatView(DetailView):
    """
    Chat View
    """

    model = Chat

    decorators = [login_required]

    template_name = "chat/chat.html"

    pk_or_slug_url = "pk"

    def get_context_data(self, **kwargs):
        session["room"] = str(self.object.pk)
        return super().get_context_data(**kwargs)


class ChatListView(TemplateView):
    """
    Chat list
    """

    decorators = [login_required]

    template_name = "chat/chat.html"
