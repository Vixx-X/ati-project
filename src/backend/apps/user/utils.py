"""
Utilities for user module
"""

from bisect import bisect_left
from datetime import datetime

from mongoengine.queryset.visitor import Q
from backend import user_manager
from backend.apps.user.models import Notification, User
from backend.apps.user.signals import friend_signal, unfriend_signal


def search_idx(collection, item):
    """
    Search index for an item
    """
    idx = bisect_left(collection, item, 0, len(collection))
    return idx if idx != len(collection) else -1


def search(collection, item):
    """
    Search for an item
    """
    idx = search_idx(collection, item)
    return collection[idx] if idx != -1 else None


def contains(collection, item):
    """
    Check if collection contains item
    """
    return search_idx(collection, item) != -1


def are_friends(user1, user2):
    """
    Check if both users are friends
    """
    return contains(user1.friends, user2)


def get_user_friends(target_user, requester=None):
    """
    Gets user friends taking account the requester-user relation
    """
    if (
        requester is None
        or target_user.config.prefer_private
        and not are_friends(target_user, requester)
    ):
        return target_user.friends
    return []


def create_notification(noti_type, receiver, sender=None):
    noti = Notification(
        type=noti_type,
        receiver=receiver,
        sender=sender,
    )
    noti.save()
    return noti


def delete_notification(notification):
    notification.delete()


def remove_friend(target_user, requester):
    if are_friends(target_user, requester):
        unfriend_signal.send(target_user, requester)
        return True
    return False


def send_friend_request(target_user, requester):
    if not are_friends(target_user, requester) and target_user.accept_friend_request:
        friend_signal.send(target_user, requester)
        return True
    return False


def respond_to_friend_request(notification, veredict):
    if not notification.is_friend_request():
        raise Exception("Notification is not friend request")
    if veredict:
        friend_signal.send(notification.sender, notification.receiver)
    delete_notification(notification)


def accept_friend_request(notification):
    respond_to_friend_request(notification, True)


def deny_friend_request(notification):
    respond_to_friend_request(notification, False)


def search_users(term):
    from backend.apps.user.models import User

    return User.objects.filter(Q(username__icontains=term) or Q(email__icontains=term))


def get_common_friends(user1, user2):
    # this is bad, but no time for aggregations
    ret = []
    for f in user1.friends:
        if f in user2.friends:
            ret.append(f)
    return ret


def get_common_friends_number(user1, user2):
    return len(get_common_friends(user1, user2))


def create_user(**kwargs):
    user = User(**kwargs)
    user.active = True
    user.is_primary = True
    user.password = user_manager.hash_password(user.password)
    user.email_confirmed_at = datetime.utcnow()
    
    return user

def are_pending(sender, receiver):
    notification = receiver.notifications.filter(type=Notification.FRIEND_REQUEST, sender=sender)

    return notification
