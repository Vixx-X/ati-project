import json
import os
from datetime import datetime

from PIL import Image

field_map = {
    "nombre": "name",
    "email": "email",
    "descripcion": "description",
    "color": "colors",
    "libro": "books",
    "video_juego": "games",
    "musica": "music",
    "lenguajes": "langs",
    "ci": "ci",
    "genero": "gender",
    "fecha_nacimiento": "birth_date",
    "imagen": "image",
}


def clean_date(value):
    try:
        return datetime.strptime(value, "%d/%m/%Y")
    except:
        return datetime.now


def clean_gender(value):
    gender_map = {
        "masculino": "M",
        "femenino": "F",
    }
    if not isinstance(value, str):
        value = "O"
    return gender_map.get(value, "X")


def clean_list(value):
    if isinstance(value, list):
        return value
    return [val.strip() for val in value.split(",")]


def clean_ci(value):
    if isinstance(value, str):
        value = value.replace(".", "")
    return value


def clean_description(value):
    SIZE_OF_DESC = 1024
    if len(value) > SIZE_OF_DESC:
        value = value[: SIZE_OF_DESC - 3] + "..."
    return value


def import_user(file, dirname=None, dry_run=False):
    """
    Given a path it retrieve information for that user and profile photo
    """
    from backend import user_manager
    from backend.apps.media.utils import save_media
    from backend.apps.user.models import User, clean_username
    from backend.apps.user.utils import create_user

    user_data = json.load(file)
    kwargs = {}
    for field in user_data:
        model_attr = field_map.get(field)

        if model_attr is None:
            continue
        data = user_data[field]

        if model_attr == "birth_date":
            data = clean_date(data)

        if model_attr == "gender":
            data = clean_gender(data)

        if model_attr == "description":
            data = clean_description(data)

        if model_attr == "ci":
            data = clean_ci(data)

        if model_attr in [
            "colors",
            "books",
            "games",
            "music",
            "langs",
        ]:
            data = clean_list(data)

        # special cases
        if model_attr == "name":
            fullname = data.split()
            size = len(fullname)
            kwargs["first_name"] = " ".join(fullname[: size // 2]) or ""
            kwargs["last_name"] = " ".join(fullname[size // 2 :]) or ""
            kwargs["username"] = clean_username("_".join(fullname).lower())
        elif model_attr == "image" and dirname:
            filename = os.path.join(dirname, data)
            if not os.path.isfile(filename):
                continue
            img = Image.open(filename)
            kwargs["profile_photo"] = save_media(img, dry_run=dry_run)
        else:
            kwargs[model_attr] = data

    # ci is default password
    kwargs["password"] = str(kwargs.get("ci", "<SECRET>"))

    user = create_user(**kwargs)

    return user


def loaddata(path, dry_run=False):
    """
    In this case we only need to import json for users, and its images
    given a path folder and having a special file structure,
    but this concept could be extended.
    """
    try:
        users = []
        for root, dirs, _ in os.walk(path):
            for file in dirs:
                dirname = os.path.join(root, file)
                filename = os.path.join(dirname, "perfil.json")

                with open(filename, "r", encoding="utf-8") as f:
                    users.append(import_user(f, dirname, dry_run))

        if not dry_run:
            for user in users:
                user.save()

        print(f"Loaded {len(users)} users.")
    except:
        raise Exception(f"A critical error ocurred.")
