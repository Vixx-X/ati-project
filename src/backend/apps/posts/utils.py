from backend.apps.posts.models import Post
from backend.apps.user.signals import check_comment_signal


def _get_two_last_obj_with_path(path_list):
    size = len(path_list)
    if not size:
        raise Exception("path_list cannot be empty")
    pk = path_list[0]
    if size == 1:
        post = Post.objects.get(id=pk)
        return post, post
    parent, son = _get_obj_with_path(path_list[1:])
    parent = son
    son = son.comments.get(id=pk)
    return parent, son


def get_two_last_obj_with_path(path):
    return _get_two_last_obj_with_path(path.split("/")[::-1])


def get_object_by_path(path):
    _, son = get_object_by_path(path)
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

    # notify son author
    check_comment_signal.send(comment.author, son.author)


def get_comments(obj, page=1, size=10):
    start = (page - 1) * size
    end = start + size
    ret = []
    for com in obj.comments[start:end]:
        curr = com.as_dict()
        childs = []
        for child in com.comments[: size / 2]:
            childs.append(child.as_dict())
        setattr(curr, "comments", childs)
        ret.append(curr)
    return ret


def get_comments_by_path(path, page, size):
    comment = get_object_by_path(path)
    return get_comments(comment, page, size)
