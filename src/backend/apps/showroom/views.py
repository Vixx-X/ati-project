"""
Views for the showroom module.
"""

from flask.helpers import url_for
from backend.utils.views import BaseView
from flask_babel import lazy_gettext as _ # for i18n

def get_tag(tag):
    """
    Get tag item to translate with ownership if the case
    """

    if isinstance(tag, list):
        label, owner = tag
        return (_(label) + ' - %s') % owner
    return _(tag)

class Index(BaseView):
    """
    Index View to showcase all rooms.
    """

    template_name = "showroom/index.html"
    title = _("Showroom Showcase")
    list_of_rooms = "list_of_rooms"

    def get_context_data(self):
        """
        Place the list_of_rooms in the context
        """
        from . import urls
        list_of_rooms = getattr(urls, self.list_of_rooms)

        urls_list = {
            get_tag(tag): url_for(f"showroom.{name}") for name, tag in list_of_rooms
        }
        return {"list": urls_list, "title": self.title}


class Components(Index):
    """
    Index View to showcase all components.
    """

    title = _("Components Showcase")
    list_of_rooms = "list_of_components"



class Views(Index):
    """
    Index View to showcase all views.
    """

    title = _("Views Showcase")
    list_of_rooms = "list_of_views"


class Buttons(BaseView):
    """
    Showcase for button component.
    """

    template_name = "showroom/buttons.html"


class Header(BaseView):
    """
    Showcase for header component.
    """

    template_name = "showroom/header.html"


class UserIcon(BaseView):
    """
    Showcase for user-icon component.
    """

    template_name = "showroom/user-icon.html"


class Card(BaseView):
    """
    Showcase for card component.
    """

    template_name = "showroom/card.html"


class Header2(BaseView):
    """
    Showcase for header2 component.
    """

    template_name = "showroom/header2.html"

class Comments(BaseView):
    """
    Showcase for comments-users component.
    """

    template_name = "showroom/comments-users.html"


class Footers(BaseView):
    """
    Showcase for footer component.
    """

    template_name = "showroom/footer.html"


class Heading(BaseView):
    """
    Showcase for heading component.
    """

    template_name = "showroom/heading.html"


class LongCards(BaseView):
    """
    Showcase for long cards component.
    """

    template_name = "showroom/long-cards.html"

class Notification(BaseView):
    """
    Showcase for notification component.
    """

    template_name = "showroom/notification.html"


class SearchButton(BaseView):
    """
    Showcase for search component.
    """

    template_name = "showroom/search-button.html"


class Chat(BaseView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/chat.html"

class ListFriends(BaseView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/list-friends.html"
class HeaderPublication(BaseView):
    """
    Showcase for header publication component.
    """
    template_name = "showroom/header-publication.html"


class Muro(BaseView):
    """
    Showcase for muro view.
    """

    template_name = "showroom/muro.html"

class Home(BaseView):
    """
    Showcase for home view.
    """

    template_name = "showroom/home.html"

class LogIn(BaseView):
    """
    Showcase for login view.
    """

    template_name = "showroom/login.html"

class InputLabel(BaseView):
    """
    Showcase for inputLabel component.
    """
    template_name = "showroom/input-label.html"

class RadioButton(BaseView):
  """
  Showcase for RadioButton component.
  """
  template_name = "showroom/radio-button.html"

class BooleanButton(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/boolean-button.html"

class DropDownList(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/drop-down-list.html"
  
class ElementFriendList(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/element-friend-list.html"
  
class FooterMobile(BaseView):
  """
  Showcase for footer mobile component.
  """
  template_name = "showroom/footer-mobile.html"

class Register(BaseView):
  """
  Showcase for register component.
  """
  template_name = "showroom/register.html"

class Notifications(BaseView):
  """
  Showcase for footer mobile component.
  """
  template_name = "showroom/notifications.html"
  
class ListChats(BaseView):
  """
  Showcase for chat list component.
  """
  template_name = "showroom/list-chats.html"

class Configurations(BaseView):
  """
  Showcase for configuration view.
  """
  template_name = "showroom/configurations.html"

class Profile1(BaseView):
  """
  Showcase for profile1 view.
  """
  template_name = "showroom/profile1.html"

class CreatePublications(BaseView):
  """
  Showcase for profile1 view.
  """
  template_name = "showroom/CreatePublications.html"
  
class MobileNavMenu(BaseView):
  """
  Showcase for mobile nav menu component.
  """
  template_name = "showroom/mobile-navmenu.html"

class ListComments(BaseView):
  """
  Showcase for profile1 view.
  """
  template_name = "showroom/list-comments.html"
