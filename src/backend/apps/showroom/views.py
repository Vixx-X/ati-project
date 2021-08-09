"""
Views for the showroom module.
"""

from flask.helpers import url_for
from backend.utils.views import TemplateView
from flask_babel import lazy_gettext as _  # for i18n


def get_tag(tag):
    """
    Get tag item to translate with ownership if the case
    """

    if isinstance(tag, list):
        label, owner = tag
        return (_(label) + " - %s") % owner
    return _(tag)


class Index(TemplateView):
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


class Buttons(TemplateView):
    """
    Showcase for button component.
    """

    template_name = "showroom/components/buttons.html"


class Header(TemplateView):
    """
    Showcase for header component.
    """

    template_name = "showroom/components/header.html"


class UserIcon(TemplateView):
    """
    Showcase for user-icon component.
    """

    template_name = "showroom/components/user-icon.html"


class Card(TemplateView):
    """
    Showcase for card component.
    """

    template_name = "showroom/components/card.html"


class Header2(TemplateView):
    """
    Showcase for header2 component.
    """

    template_name = "showroom/components/header2.html"


class Comments(TemplateView):
    """
    Showcase for comments-users component.
    """

    template_name = "showroom/components/comments-users.html"


class Footers(TemplateView):
    """
    Showcase for footer component.
    """

    template_name = "showroom/components/footer.html"


class Heading(TemplateView):
    """
    Showcase for heading component.
    """

    template_name = "showroom/components/heading.html"


class LongCards(TemplateView):
    """
    Showcase for long cards component.
    """

    template_name = "showroom/components/long-cards.html"


class Notification(TemplateView):
    """
    Showcase for notification component.
    """

    template_name = "showroom/components/notification.html"


class SearchButton(TemplateView):
    """
    Showcase for search component.
    """

    template_name = "showroom/components/search-button.html"


class Chat(TemplateView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/components/chat.html"


class ListFriends(TemplateView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/components/list-friends.html"


class HeaderPublication(TemplateView):
    """
    Showcase for header publication component.
    """
    template_name = "showroom/components/header-publication.html"


class Muro(TemplateView):
    """
    Showcase for muro view.
    """

    template_name = "showroom/views/muro.html"


class Home(TemplateView):
    """
    Showcase for home view.
    """

    template_name = "showroom/views/home.html"


class LogIn(TemplateView):
    """
    Showcase for login view.
    """

    template_name = "showroom/views/login.html"


class InputLabel(TemplateView):
    """
    Showcase for inputLabel component.
    """
<<<<<<< HEAD

    template_name = "showroom/input-label.html"


class RadioButton(TemplateView):
    """
    Showcase for RadioButton component.
    """

    template_name = "showroom/radio-button.html"


class BooleanButton(TemplateView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/boolean-button.html"


class DropDownList(TemplateView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/drop-down-list.html"


class ElementFriendList(TemplateView):
    """
    Showcase for chat component.
    """

    template_name = "showroom/element-friend-list.html"


class FooterMobile(TemplateView):
    """
    Showcase for footer mobile component.
    """

    template_name = "showroom/footer-mobile.html"


class Register(TemplateView):
    """
    Showcase for register component.
    """

    template_name = "showroom/register.html"


class Notifications(TemplateView):
    """
    Showcase for footer mobile component.
    """

    template_name = "showroom/notifications.html"


class ListChats(TemplateView):
    """
    Showcase for chat list component.
    """

    template_name = "showroom/list-chats.html"


class Configurations(TemplateView):
    """
    Showcase for configuration view.
    """

    template_name = "showroom/configurations.html"


class Profile1(TemplateView):
    """
    Showcase for profile1 view.
    """

    template_name = "showroom/profile1.html"


class CreatePublications(TemplateView):
    """
    Showcase for profile1 view.
    """

    template_name = "showroom/CreatePublications.html"


class MobileNavMenu(TemplateView):
    """
    Showcase for mobile nav menu component.
    """

    template_name = "showroom/mobile-navmenu.html"


class ListComments(TemplateView):
    """
    Showcase for profile1 view.
    """

    template_name = "showroom/list-comments.html"
=======
    template_name = "showroom/components/input-label.html"

class RadioButton(BaseView):
  """
  Showcase for RadioButton component.
  """
  template_name = "showroom/components/radio-button.html"

class BooleanButton(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/components/boolean-button.html"

class DropDownList(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/components/drop-down-list.html"
  
class ElementFriendList(BaseView):
  """
  Showcase for chat component.
  """
  template_name = "showroom/components/element-friend-list.html"
  
class FooterMobile(BaseView):
  """
  Showcase for footer mobile component.
  """
  template_name = "showroom/components/footer-mobile.html"

class Register(BaseView):
  """
  Showcase for register component.
  """
  template_name = "showroom/views/register.html"

class Notifications(BaseView):
  """
  Showcase for footer mobile component.
  """
  template_name = "showroom/views/notifications.html"
  
class ListChats(BaseView):
  """
  Showcase for chat list component.
  """
  template_name = "showroom/components/list-chats.html"

class Configurations(BaseView):
  """
  Showcase for configuration view.
  """
  template_name = "showroom/views/configurations.html"

class Profile(BaseView):
  """
  Showcase for profile view.
  """ 
  template_name = "showroom/views/profile.html"
  
class MobileNavMenu(BaseView):
  """
  Showcase for mobile nav menu component.
  """
  template_name = "showroom/components/mobile-navmenu.html"

class ListComments(BaseView):
  """
  Showcase for profile1 view.
  """
  template_name = "showroom/components/list-comments.html"

class ChatView(BaseView):
  """
  Showcase for chat view.
  """
  template_name = "showroom/views/chatView.html"

class CreatePublication(BaseView):
  """
  Showcase for create publication view.
  """
  template_name = "showroom/views/create-publication.html"

class ForgotPassword(BaseView):
  """
  Showcase for forgot password view.
  """
  template_name = "showroom/views/forgotpassword.html"

class FriendList(BaseView):
  """
  Showcase for friend list view.
  """
  template_name = "showroom/views/friend-list.html"

class LandingPage(BaseView):
  """
  Showcase for Landing view.
  """
  template_name = "showroom/views/landing-page.html"

class ModifyPublication(BaseView):
  """
  Showcase for Landing view.
  """
  template_name = "showroom/views/modify-publication.html"

class Post(BaseView):
  """
  Showcase for Post view.
  """
  template_name = "showroom/views/post.html"

class ProfileDescription(BaseView):
  """
  Showcase for Profile Description view.
  """
  template_name = "showroom/views/profile-description.html"

class ProfileEdit(BaseView):
  """
  Showcase for Profile Edit view.
  """
  template_name = "showroom/views/profile-edit.html"

class SearchPage(BaseView):
  """
  Showcase for Profile Edit view.
  """
  template_name = "showroom/views/search-page.html"
>>>>>>> origin/develop
