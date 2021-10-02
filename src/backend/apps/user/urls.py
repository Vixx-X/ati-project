"""
Urls for user module/blueprint
"""

from flask.helpers import url_for
from flask_user.decorators import login_required, current_user
from mongoengine.queryset.visitor import Q
from flask import redirect

from backend.apps.chat.models import Chat
from . import bp, views
from .models import User

# users
bp.add_url_rule("/<string:username>", view_func=views.PageView.as_view("page"))
bp.add_url_rule(
    "/<string:username>/profile", view_func=views.ProfileView.as_view("profile")
)
bp.add_url_rule(
    "/<string:username>/friends", view_func=views.FriendView.as_view("friends")
)

# current user
bp.add_url_rule("/", view_func=views.PageView.as_view("mypage"))
bp.add_url_rule(
    "/notifications", view_func=views.NotificationView.as_view("notification")
)
bp.add_url_rule("/config", view_func=views.ConfigView.as_view("config"))


# misc
bp.add_url_rule("/search", view_func=views.SearchView.as_view("search"))
bp.add_url_rule("/check_email", view_func=views.CheckEmailView.as_view("check_email"))

# chats
@bp.route("/<string:username>/chat")
@login_required
def chat(username):
    user1 = current_user._get_current_object()
    user2 = User.objects.get_or_404(username=username)
    qs = Chat.objects.filter(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1))
    chat = qs[0] if qs else Chat(user1=user1, user2=user2)
    chat.save()
    return redirect(url_for("chat.chat", pk=str(chat.pk)))


