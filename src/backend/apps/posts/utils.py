from mongoengine.queryset.visitor import Q
from backend.apps.posts.models import Post
from backend.apps.user.signals import check_comment_signal
from backend.apps.user.utils import are_friends


def _get_two_last_obj_with_path(path_list):
    size = len(path_list)
    if not size:
        raise Exception("path_list cannot be empty")
    pk = path_list[0]
    if size == 1:
        post = Post.objects.get(id=pk)
        return post, post
    parent, son = _get_two_last_obj_with_path(path_list[1:])
    parent = son
    son = son.comments.get(id=pk)
    return parent, son


def get_two_last_obj_with_path(path):
    return _get_two_last_obj_with_path(path.split("/")[::-1])


def get_object_by_path(path):
    _, son = _get_two_last_obj_with_path(path)
    return son


def save_comment_by_path(path, comment):
    """
    Saving comment inserting it in root comment or post, given that we
    only have 2-depth comments
    """
    parent, son = get_two_last_obj_with_path(path)
    if isinstance(parent, Post) and not isinstance(son, Post):
        son.comments.append(comment)
    else:
        parent.comments.append(comment)

    post = get_object_by_path(path.split("/")[0])
    post.save()

    # notify son author
    check_comment_signal.send(comment.author, son.author)


def get_comments(obj, page=1, size=10, path=None):
    start = (page - 1) * size
    end = start + size
    raiz = []
    for com in obj.comments[start:end]:
        curr = com.as_dict()
        childs = []
        for child in com.comments[: size / 2]:
            c = child.as_dict()
            c["reply"] = path.split("/") + [curr["id"], c["id"]]
            childs.append(c)
        setattr(curr, "comments", childs)
        curr["reply"] = path.split("/") + [curr["id"]]
        junior = {"comments": curr, "more": path.split("/") + [curr["id"]]}
        raiz.append(junior)
    ret = {"comments": raiz}
    if len(raiz) == size:
        ret["more"] = path.split("/")
    return raiz


def get_comments_by_path(path, page, size):
    comment = get_object_by_path(path)
    return get_comments(comment, page, size, path)


def get_main_posts(requester):
    return Post.objects.filter(Q(public=True) or Q(author__in=requester.friends)).order_by("-time_created")


def get_posts_by_user(user, requester):
    friends = are_friends(user, requester)
    priv_filter = Q() if friends else (Q(public=True) | Q(author=requester))
    filter_param = Q(author=user) & priv_filter
    return Post.objects.filter(filter_param).order_by("-time_created")

