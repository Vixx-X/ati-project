"""
Urls for user module/blueprint
"""

from . import bp, views

# users
bp.add_url_rule("/<string:username>", view_func=views.ProfileView.as_view("profile"))
bp.add_url_rule(
    "/<string:username>/friends", view_func=views.FriendView.as_view("friend")
)
bp.add_url_rule(
    "/friends", view_func=views.FriendView.as_view("friend_detail")
)

# current user
bp.add_url_rule("/profile", view_func=views.ProfileView.as_view("profile_detail"))
bp.add_url_rule(
    "/notifications", view_func=views.NotificationView.as_view("notification")
)
bp.add_url_rule("/config", view_func=views.ConfigView.as_view("config"))

# chats
bp.add_url_rule("/chat", view_func=views.ChatView.as_view("chat"))

# misc
bp.add_url_rule("/search", view_func=views.SearchView.as_view("search"))
bp.add_url_rule("/check_email", view_func=views.CheckEmailView.as_view("check_email"))
