from wtforms.fields.simple import FileField, MultipleFileField
from backend.apps.media.utils import create_or_replace_from_form


class FormMediaMixin:
    def get_all_media_fields(self):
        ret = [
            field
            for _, field in self._fields.items()
            if isinstance(field, FileField) or isinstance(field, MultipleFileField)
        ]
        return ret

    def __init__(self, *args, **kwargs) -> None:
        obj = kwargs["obj"]
        super().__init__(*args, **kwargs)
        for field in self.get_all_media_fields():
            setattr(field, "media", getattr(obj, field.name))

    def populate_obj(self, obj, **kwargs):
        super().populate_obj(obj, **kwargs)

        for field in self.get_all_media_fields():
            media = create_or_replace_from_form(
                getattr(obj, field.name),
                field.name,
            )
            setattr(obj, field.name, media)

        obj.save()
