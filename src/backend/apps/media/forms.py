"""
Form Media mixins
"""

from wtforms.fields.simple import FileField, MultipleFileField

from backend.apps.media.utils import create_or_replace_from_form


class FormMediaMixin:
    """
    Form media mixin that handle FileField and MultipleFileField
    """

    def get_all_media_fields(self):
        """
        Get media fields
        """
        ret = [
            field
            for _, field in self._fields.items()
            if isinstance(field, (FileField, MultipleFileField))
        ]
        return ret

    def __init__(self, *args, **kwargs) -> None:
        obj = kwargs.get("obj")
        super().__init__(*args, **kwargs)
        if not self.is_submitted() and obj:
            for field in self.get_all_media_fields():
                setattr(field, "media", getattr(obj, field.name))

    def populate_obj(self, obj, **kwargs):
        """
        Save field data into object instance
        """
        media_fields = self.get_all_media_fields()
        media_aux = {field.name: getattr(obj, field.name) for field in media_fields}

        super().populate_obj(obj, **kwargs)

        for name, media in media_aux.items():
            setattr(obj, name, media)

        for field in media_fields:
            media = create_or_replace_from_form(
                getattr(obj, field.name),
                field.name,
                isinstance(field, MultipleFileField),
            )
            if media:
                setattr(obj, field.name, media)
