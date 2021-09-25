"""
Views for the friends endpoints of api module.
"""

from flask.json import jsonify
from flask import request

from backend.apps.api.errors import ResourceNotFoundError, UnauthorizedError

from backend.apps.api.decorators import login_required
from backend.apps.user.models import User, Notification
from backend.apps.user.utils import (
    delete_notification,
    get_user_friends,
    remove_friend,
    send_friend_request,
    accept_friend_request,
    deny_friend_request,
)
from backend.apps.api.views.utils import APIView
from flask_babel import gettext as _  # for i18n


class NotificationView(APIView):

    def check_veredict(self, veredict):
        """
        Check if veredict is true or false depending on frontend
        """
        return bool(veredict)

    def get_notification(self, notification_id, friend_request=False):
        """
        Given notification_id get notification
        """
        kwargs = {
            "id": notification_id,
            "receiver": self.user,
        }
        if friend_request:
            kwargs["type"]: Notification.FRIEND_REQUEST
        try:
            return Notification.objects.get(**kwargs)
        except:
            raise ResourceNotFoundError(
                404, msg=_("Target notification (%s) not found") % notification_id
            )

    def post(self, notification_id):
        notification = self.get_notification(
            notification_id,
            friend_request=True,
        )
        veredict = request.get_json()["veredict"]
        if self.check_veredict(veredict):
            accept_friend_request(notification)
            return jsonify({"msg": _("You are now friends.")})
        deny_friend_request(notification)
        return jsonify({"msg": _("Rejected")})

    def delete(self, notification_id):
        notification = self.get_notification(
            notification_id,
        )
        delete_notification(notification)
        return jsonify({"msg": _("Notification deleted.")})


class FriendView(APIView):

    decorators = [login_required]

    def targer_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            raise ResourceNotFoundError(
                404, msg=_("Target user (%s) not found") % username
            )

    def get(self, username):
        """
        Get username's friends
        """
        user = self.targer_user(username)
        return jsonify({"friends": get_user_friends(user, requester=self.user)})

    def post(self, username):
        """
        Send username's a friend request
        """
        user = self.targer_user(username)
        if send_friend_request(user, requester=self.user):
            return {"ok": ""}
        raise UnauthorizedError(msg="You are not allowed.")

    def delete(self, username):
        """
        Unfriend username
        """
        user = self.targer_user(username)
        if remove_friend(user, requester=self.user):
            return {"msg": "You are not friends anymore"}
        raise UnauthorizedError(msg="You are not allowed.")
