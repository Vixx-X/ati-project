"""
Views for the friends endpoints of api module.
"""

from backend.apps.api.errors import UnauthorizedError

from backend.apps.user.models import User, Notification
from backend.apps.user.utils import (
    delete_notification,
    get_user_friends,
    remove_friend,
    send_friend_request,
    accept_friend_request,
    deny_friend_request,
)
from backend.apps.api.views.utils import APIDetailView
from flask_babel import gettext as _  # for i18n


class NotificationView(APIDetailView):

    resource = Notification

    def get_resource_filter(self):
        kwargs = {
            "id": self.kwargs["id"],
            "receiver": self.user,
        }
        if self.method.lower() == "post":  # post is only for friend requests
            kwargs["type"] = Notification.FRIEND_REQUEST
        return kwargs

    def post(self, data, **kwargs):

        veredict = data["veredict"]
        notification = self.object

        if veredict:
            accept_friend_request(notification)
            return self.response(message=_("You are now friends."))
        deny_friend_request(notification)
        return self.response(message=_("Rejected."))

    def delete(self, **kwargs):
        notification = self.object
        delete_notification(notification)
        return self.response(message=_("Notification deleted."))


class FriendView(APIDetailView):

    resource = User
    look_up_attr = "username"

    def get(self, **kwargs):
        """
        Get username's friends
        """
        user = self.object
        start = (self.page - 1) * self.size
        end = start + self.size
        return self.response(
            data=get_user_friends(user, requester=self.user)[start:end]
        )

    def post(self, **kwargs):
        """
        Send username's a friend request
        """
        user = self.object
        if send_friend_request(user, requester=self.user):
            return self.response(status=201)
        raise UnauthorizedError()

    def delete(self, **kwargs):
        """
        Unfriend username
        """
        user = self.object
        if remove_friend(user, requester=self.user):
            return self.response(message=_("You are not friends anymore"))
        raise UnauthorizedError()
