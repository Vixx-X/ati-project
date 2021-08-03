"""
Urls for showroom module/blueprint
"""

from . import bp, views


VA = "Vittorio Adesso"
GU = "Gabriela Ustariz"
ED = "Eduardo Suarez"
DV = "Daniel Vieira"

list_of_rooms = [
    ("components", "Components"),
    ("views", "Views"),
]

bp.add_url_rule("/", view_func=views.Index.as_view("index"))

##############
# Components #
##############

list_of_components = [
    ("buttons", ["Buttons", GU]),
    ("header", ["Header", GU]),
    ("user_icon", ["User Icons", VA]),
    ("card", "Card - Daniel Vieira"),
    ("header2", "Main Header - Gabriela Ustariz"),
    ("comments-users", "Comments of Users - Vittorio Adesso"),
    ("footer", "Footer - Eduardo Saurez"),
    ("heading", "Heading - Daniel Vieira"),
    ("long-cards", "Long Cards - Daniel Vieira"),
    ("notification", "Notification - Vittorio Adesso"),
    ("search-button", "Search Button - Eduardo Suarez"),
    ("chat", "Chat - Eduardo Suarez"),
    ("header_publication", "Header Publication - DanielVieria"),
    ("input-label", "Input Label - Daniel Vieria"),
    ("list-friends", "list-friends - Eduardo Suarez"),
    ("boolean-button", "Boolean Button - Daniel Vieria"),
    ("drop-down-list", "Drop Down List - Eduardo Suarez"),
    ("footer-mobile", "Footer Mobile - Daniel Vieria"),
]

bp.add_url_rule("/components/", view_func=views.Components.as_view("components"))
bp.add_url_rule("/buttons/", view_func=views.Buttons.as_view("buttons"))
bp.add_url_rule("/header/", view_func=views.Header.as_view("header"))
bp.add_url_rule("/user-icon/", view_func=views.UserIcon.as_view("user_icon"))
bp.add_url_rule("/card/", view_func=views.Card.as_view("card"))
bp.add_url_rule("/header2/", view_func=views.Header2.as_view("header2"))
bp.add_url_rule("/comments-users/", view_func=views.Comments.as_view("comments-users"))
bp.add_url_rule("/footer/", view_func=views.Footers.as_view("footer"))
bp.add_url_rule("/heading/", view_func=views.Heading.as_view("heading"))
bp.add_url_rule("/long-cards/", view_func=views.LongCards.as_view("long-cards"))
bp.add_url_rule("/notification/", view_func=views.Notification.as_view("notification"))
bp.add_url_rule(
    "/search-button/", view_func=views.SearchButton.as_view("search-button")
)
bp.add_url_rule("/chat/", view_func=views.Chat.as_view("chat"))
bp.add_url_rule("/list-friends/", view_func=views.ListFriends.as_view("list-friends"))
bp.add_url_rule(
    "/header-publication/",
    view_func=views.HeaderPublication.as_view("header_publication"),
)
bp.add_url_rule("/input-label/", view_func=views.InputLabel.as_view("input-label"))
bp.add_url_rule("/radio-button/", view_func=views.RadioButton.as_view("radio-button"))


#########
# Views #
#########

list_of_views = [
    ("muro", "Muro"),
    ("home", "Home"),
    ("login", "LogIn"),
    ("register", "Register"),
    ("configurations", "Configurations"),
    ("notifications", "Notifications"),
    ("profile1", "Profile"),
    ("boolean-button", "Boolean Button - Daniel Vieria"),
    ("drop-down-list", "Drop Down List - Eduardo Suarez"),
    ("footer-mobile", "Footer Mobile - Daniel Vieria"),
    ("list-chats", "List Chats - Daniel Vieria"),
    ("element-friend-list", "Element Friend List - Eduardo Suarez"),
    ("CreatePublications", "CreatePublications - Eduardo Suarez"),
    ("mobile-navmenu", "Mobile Nav Menu - Gabriela Uztariz"),
    ("list-comments", "List Comments - Eduardo Suarez"),
]

bp.add_url_rule("/views/", view_func=views.Views.as_view("views"))
bp.add_url_rule("/muro/", view_func=views.Muro.as_view("muro"))
bp.add_url_rule("/home/", view_func=views.Home.as_view("home"))
bp.add_url_rule("/login/", view_func=views.LogIn.as_view("login"))
bp.add_url_rule(
    "/boolean-button/", view_func=views.BooleanButton.as_view("boolean-button")
)
bp.add_url_rule(
    "/drop-down-list/", view_func=views.DropDownList.as_view("drop-down-list")
)
bp.add_url_rule(
    "/element-friend-list/",
    view_func=views.ElementFriendList.as_view("element-friend-list"),
)
bp.add_url_rule(
    "/footer-mobile/", view_func=views.FooterMobile.as_view("footer-mobile")
)
bp.add_url_rule("/register/", view_func=views.Register.as_view("register"))
bp.add_url_rule("/list-chats/", view_func=views.ListChats.as_view("list-chats"))
bp.add_url_rule(
    "/notifications/", view_func=views.Notifications.as_view("notifications")
)
bp.add_url_rule(
    "/configurations/", view_func=views.Configurations.as_view("configurations")
)
bp.add_url_rule("/profile1/", view_func=views.Profile1.as_view("profile1"))
bp.add_url_rule(
    "/CreatePublications/",
    view_func=views.CreatePublications.as_view("CreatePublications"),
)
bp.add_url_rule(
    "/mobile-navmenu/", view_func=views.MobileNavMenu.as_view("mobile-navmenu")
)
bp.add_url_rule(
    "/list-comments/", view_func=views.ListComments.as_view("list-comments")
)
