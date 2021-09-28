"""
Views for the core app.
"""

from flask_user import login_required
from backend.apps.posts.utils import get_main_posts
from backend.apps.user.utils import get_common_friends

from backend.utils.views import TemplateView

# from flask_babel import gettext as _ # for i18n


class Home(TemplateView):
    """
    Home of the application.
    """

    decorators = [login_required]
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        friends = self.user.friends
        for friend in friends:
            setattr(friend, "common_friends", get_common_friends(friend, self.user),)
        ctx["posts"] = get_main_posts(self.user)
        ctx["friends"] = friends
        return  ctx


class LandingPage(TemplateView):
    """
    Landing page for unauthenticated clients.
    """

    template_name = "landing-page.html"
