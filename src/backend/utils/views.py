import mongoengine as db
from flask import redirect, render_template, request
from flask.views import View
from flask_user import current_user

# from flask_babel import gettext as _ # for i18n


class TemplateMixin:

    template_name = None

    def get_template_name(self):
        """
        Return the template_name of class if it is set, raise NotImplementedError otherwise.
        """
        if self.template_name is None:
            raise NotImplementedError("No template_name, did you forget to declare it?")
        return self.template_name

    def render_template(self, context):
        """
        Method to render template given a context
        """
        return render_template(self.get_template_name(), **context)

    def get_context_data(self, **kwargs):
        """
        Stud method to get context data
        """
        return kwargs


class TemplateView(View, TemplateMixin):
    """
    Mixin View to shortcut basic functionalities.
    """

    methods = ["GET"]

    def dispatch_request(self, *args, **kwargs):  # pylint: disable=R0201
        return self.render_template(self.get_context_data())


class FormMixin(TemplateMixin):

    form_class = None
    success_url = None

    def get_form_kwargs(self):
        """
        Return arguments for form
        """
        return {}

    def get_form_class(self):
        """
        Return the form class to use
        """
        if self.form_class is None:
            raise NotImplementedError("No form_class, did you forget to delcare it?")
        return self.form_class

    def get_form(self):
        """
        Return an instance of the form_class
        """
        return self.get_form_class()(**self.get_form_kwargs())

    def form_invalid(self, form, *args, **kwargs):  # pylint: disable=R0201
        """
        If the form is invalid, render the invalid form.
        """
        return self.render_template(self.get_context_data(form=form))

    def get_success_url(self):
        """
        Return a url to redirect after processing a valid form
        """
        if not self.success_url:
            raise NotImplementedError("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

    def form_valid(self, form, *args, **kwargs):  # pylint: disable=R0201
        """
        Return a url to redirect after processing a valid form
        """
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        """
        Add form to the context
        """
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def get(self, *args, **kwargs):
        """
        Flow of event when rquest method is GET
        """
        return self.render_template(self.get_context_data(*args, **kwargs))

    def post(self, *args, **kwargs):
        """
        Flow of event when rquest method is POST
        """
        form = self.get_form()
        if form.validate_on_submit():
            return self.form_valid(form, *args, **kwargs)
        return self.form_invalid(form, *args, **kwargs)


class FormView(View, FormMixin, TemplateMixin):
    """
    Mixin View to shortcut basic functionalities of a view with a single form.
    """

    methods = ["GET", "POST"]

    def dispatch_request(self, *args, **kwargs):
        self.request = request
        self.args = request.args
        self.kwargs = kwargs
        self.method = request.method
        self.user = current_user._get_current_object()  # current user
        if self.method == "GET":
            return self.get(*args, **kwargs)
        return self.post(*args, **kwargs)


class UpdateView(View, FormMixin, TemplateMixin):
    """
    Mixin View to shortcut basic functionalities of a view with a single form.
    """

    methods = ["GET", "POST"]
    pk_or_slug_url = "id"
    model_pk = "_id"
    model = None

    def get_form_kwargs(self):
        """
        Provide Initial data to the form
        """
        kwargs = super().get_form_kwargs()
        if self.object:
            kwargs["obj"] = self.object
        return kwargs

    def get_model(self, *args, **kwargs):
        """
        Return the model class to use
        """
        if not self.model:
            raise NotImplementedError("Model not configured.")
        return self.model

    def get_object(self, *args, **kwargs):
        """
        Return object give the model and lookup attributes
        """
        key = kwargs.get(self.pk_or_slug_url)
        if key is None:
            return None
        try:
            return self.get_model(*args, **kwargs).get(**{self.model_pk: key})
        except db.MultipleObjectsReturned:
            raise db.MultipleObjectsReturned(
                f"The lookup (self.model_pk) argument is not unique"
            )
        except db.DoesNotExist:
            return None

    def form_valid(self, form, *args, **kwargs):
        """
        Save form data with populate_obj method of form
        """
        form.populate_obj(self.object)
        return super().form_valid(form, *args, **kwargs)

    def dispatch_request(self, *args, **kwargs):
        self.request = request
        self.args = request.args
        self.method = request.method
        self.user = current_user._get_current_object()  # current user
        self.object = self.get_object(*args, **kwargs)
        if self.method == "GET":
            return self.get(*args, **kwargs)
        return self.post(*args, **kwargs)
