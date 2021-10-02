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
    ("chat", ["Chat", GU]),
    ("comments-users", ["Comments of Users", VA]),
    ("drop-down-list", ["Drop Down List", ED]),
    ("element-friend-list", ["User Element of list", ED]),
    ("footer-mobile", ["Footer Mobile", DV]),
    ("footer", ["Footer", ED]),
    ("header", ["Header", GU]),
    ("header2", ["Home Header", GU]),
    ("heading", ["Heading", DV]),
    ("input-label", ["Input Label", DV]),
    ("list-chats", ["List Chats", VA]),
    ("list-comments", ["List Comments", ED]),
    ("list-friends", ["List Friends", ED]),
    ("long-cards", ["Long Card", DV]),
    ("mobile-navmenu", ["Nav Menu Profile", VA]),
    ("notification", ["Notification", VA]),
    ("radio-button", ["Radio Button", DV]),
    ("search-button", ["Search Button", ED]),
    ("user_icon", ["User Icons", VA]),
]

bp.add_url_rule("/all_components/", view_func=views.Components.as_view("components"))
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
bp.add_url_rule(
    "/mobile-navmenu/", view_func=views.MobileNavMenu.as_view("mobile-navmenu")
)
bp.add_url_rule(
    "/list-comments/", view_func=views.ListComments.as_view("list-comments")
)
bp.add_url_rule("/list-chats/", view_func=views.ListChats.as_view("list-chats"))
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


#########
# Views #
#########

list_of_views = [
    ('chat.chat-list', ["Chat", GU]),
    ("configurations", ["Configuratios", ED]),
    ("createpublication", ["Create Publication", ED]),
    ("forgotpassword", ["Forgot Password", VA]),
    ("friendlist", ["Friend List", ED]),
    ("home", ["Home", GU]),
    ("landingpage", ["Landing", VA]),
    # ("login", ["Login", VA]),
    ("modifypublication", ["Modify Publication", ED]),
    ("notifications", ["Notifications", DV]),
    ("post", ["Post", GU]),
    ("profile", ["Profile", GU]),
    ("profiledescription", ["Profile Description", GU]),
    ("profileedit", ["Profile Edit", DV]),
    ("register", ["Register", VA]),
    ("searchpage", ["Search Page", DV]),
]

bp.add_url_rule("/views/", view_func=views.Views.as_view("views"))
bp.add_url_rule("/chatView/", view_func=views.ChatView.as_view("chatView"))
bp.add_url_rule("/home/", view_func=views.Home.as_view("home"))
bp.add_url_rule("/login/", view_func=views.LogIn.as_view("login"))
bp.add_url_rule("/register/", view_func=views.Register.as_view("register"))
bp.add_url_rule(
    "/notifications/", view_func=views.Notifications.as_view("notifications")
)
bp.add_url_rule(
    "/configurations/", view_func=views.Configurations.as_view("configurations")
)
bp.add_url_rule("/profile/", view_func=views.Profile.as_view("profile"))
bp.add_url_rule(
    "/createpublication/",
    view_func=views.CreatePublication.as_view("createpublication"),
)
bp.add_url_rule(
    "/forgotpassword/", view_func=views.ForgotPassword.as_view("forgotpassword")
)
bp.add_url_rule("/friendlist/", view_func=views.FriendList.as_view("friendlist"))
bp.add_url_rule("/landingpage/", view_func=views.LandingPage.as_view("landingpage"))
bp.add_url_rule(
    "/modifypublication/",
    view_func=views.ModifyPublication.as_view("modifypublication"),
)
bp.add_url_rule("/post/", view_func=views.Post.as_view("post"))
bp.add_url_rule(
    "/profiledescription/",
    view_func=views.ProfileDescription.as_view("profiledescription"),
)
bp.add_url_rule("/profileedit/", view_func=views.ProfileEdit.as_view("profileedit"))
bp.add_url_rule("/searchpage/", view_func=views.SearchPage.as_view("searchpage"))
