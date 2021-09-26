"""
Signals for User module
"""

from blinker import Namespace

from backend.apps.user.models import Notification

user_signals = Namespace()

friend_signal = user_signals.signal("friend")
unfriend_signal = user_signals.signal("unfriend")
friend_request_signal = user_signals.signal("friend_request")
check_comment_signal = user_signals.signal("check_reply")
check_message_signal = user_signals.signal("check_message")
email_notification_signal = user_signals.signal("send_email")


@friend_signal.connect
def friend(sender, receiver):
    from backend.apps.user.utils import create_notification

    sender.add_friend(receiver)
    receiver.add_friend(sender)
    create_notification(Notification.FRIEND_REQUEST_ACCEPTED, receiver, sender)
    create_notification(Notification.FRIEND_REQUEST_ACCEPTED, sender, receiver)


@unfriend_signal.connect
def unfriend(sender, receiver):
    sender.remove_friend(receiver)
    receiver.remove_friend(sender)


@check_comment_signal.connect
def reply_comment(sender, receiver):
    from backend.apps.user.utils import create_notification

    create_notification(
        Notification.CHECK_RESPONSE,
        receiver=receiver,
        sender=sender,
    )


@check_comment_signal.connect
def reply_message(sender, receiver):
    from backend.apps.user.utils import create_notification

    create_notification(
        Notification.CHECK_MESSAGE,
        receiver=receiver,
        sender=sender,
    )


@friend_request_signal.connect
def friend_request(sender, receiver):
    from backend.apps.user.utils import create_notification

    create_notification(Notification.FRIEND_REQUEST, receiver, sender)


@email_notification_signal.connect
def send_email(receivers, **kwargs):
    if not isinstance(receivers, list):
        receivers = [receivers]
    # https://github.com/lingthio/Flask-User/blob/master/flask_user/email_manager.py
    for receiver in receivers:
        pass
