"""
Views for the api module.
"""

from flask_restful import Resource
from flask_wtf.csrf import generate_csrf

from flask_user import current_user
from flask import request

from backend.apps.api.decorators import login_required
from mongoengine.errors import ValidationError as MVE, NotUniqueError as MNUE
from backend.apps.api.errors import (
    NotUniqueError,
    ResourceNotFoundError,
    ValidationError,
)
from flask_babel import lazy_gettext as _

from backend.apps.api.utils import make_response  # for i18n


class APIView(Resource):
    """
    Base api view to get self.user as current user
    """

    decorators = [login_required]
    DEFAULT_PAGE_SIZE = 10
    DEFAULT_PAGE = 1

    def process_context(self):
        """
        Process context before dispatching
        """
        return

    def get_pagination(self):
        """
        Get pagination
        """
        try:
            self.page = int(self.args.get("page"))
        except Exception:
            self.page = self.DEFAULT_PAGE
        try:
            self.size = int(self.args.get("size"))
        except Exception:
            self.size = self.DEFAULT_PAGE_SIZE
        return self.page, self.size

    def get_data(self):
        return self.request.get_json()

    def dispatch_request(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = request.args
        self.request = request
        self.method = request.method
        self.user = current_user._get_current_object()  # current user
        self.get_pagination()
        self.data = self.get_data()
        self.process_context()
        kwargs["data"] = self.data
        return super().dispatch_request(*args, **kwargs)

    def response(self, data=None, message=_("Success"), status=200, **kwargs):
        """
        Format a response and append csrf (X-CSRFTOKEN)
        """
        return make_response(
            data=data,
            message=message,
            status=status,
            csrf=generate_csrf(),
            **kwargs,
        )

    def populate_obj(self, data, obj):
        """
        Populate obj with data
        """
        for field in data:
            setattr(obj, field, data[field])


class APIListView(APIView):
    """
    API View in charge of performing actions on lists
    """

    resource = None

    def get_resource_filter(self):
        """
        Override this for kwargs queryset filter
        """
        return {}

    def get_resource_kwargs(self, data):
        """
        Override this for kwargs on object initialization
        """
        return data

    def get_queryset(self):
        """
        Get the QuerySet from resource
        """
        try:
            return self.resource.objects.filter(**self.get_resource_filter()).paginate(
                page=self.page,
                per_page=self.size,
            )
        except:
            raise ResourceNotFoundError(_("Resource does not exist."))

    def process_context(self):
        self.queryset = self.get_queryset()
        self.data = self.get_data()
        return super().process_context()

    def get(self, **kwargs):
        total = self.queryset.total
        items = [item.as_dict() for item in self.queryset.items]
        count = len(items)
        return self.response(data=items, count=count, total=total)

    def post(self, data, **kwargs):
        init_data = self.get_resource_kwargs(data)
        try:
            obj = self.resource(**init_data).save()
        except MVE:
            raise ValidationError()
        except MNUE:
            raise NotUniqueError()

        return self.response(data=obj, status=201)


class APIDetailView(APIView):
    """
    API View in charge of performing common model actions
    """

    look_up_attr = "id"
    resource = None

    def get_resource_filter(self):
        """
        Override this for kwargs queryset filter
        """
        return {self.look_up_attr, self.kwargs.get(self.look_up_attr)}

    def get_object(self):
        """
        Get object
        """
        return self.resource.objects.get(**self.get_resource_filter())

    def process_context(self):
        self.object = self.get_object()
        return super().process_context()

    def delete(self, **kwargs):
        self.object.delete()
        return self.response(message=_("Resource deleted"))

    def get(self, **kwargs):
        return self.response(data=self.object)

    def update(self, data, **kwargs):
        """
        Update object flow por PUT and PATCH
        """
        try:
            self.populate_obj(data, self.object)
            self.object.save()
        except MVE:
            raise ValidationError()
        except MNUE:
            raise NotUniqueError()
        return self.response(data=self.object)

    put = patch = update
