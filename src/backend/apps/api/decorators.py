"""
Decorators for api module
"""


from functools import wraps

from flask import current_app
from flask_user.decorators import _is_logged_in_with_confirmed_email

from backend.apps.api.errors import UnauthorizedError


def login_required(view_function):
    """This decorator ensures that the current user is logged in.
    Example::
        @route('/member_page')
        @login_required
        def member_page():  # User must be logged in
            ...
    If USER_ENABLE_EMAIL is True and USER_ENABLE_CONFIRM_EMAIL is True,
    this view decorator also ensures that the user has a confirmed email address.
    | Calls unauthorized_view() when the user is not logged in
        or when the user has not confirmed their email address.
    | Calls the decorated view otherwise.
    """

    @wraps(view_function)  # Tells debuggers that is is a function wrapper
    def decorator(*args, **kwargs):
        user_manager = current_app.user_manager

        # User must be logged in with a confirmed email address
        allowed = _is_logged_in_with_confirmed_email(user_manager)
        if not allowed:
            # Redirect to unauthenticated page
            raise UnauthorizedError()

        # It's OK to call the view
        return view_function(*args, **kwargs)

    return decorator
