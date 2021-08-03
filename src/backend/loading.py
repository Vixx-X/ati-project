"""
Dynamic import of classes and modules.

Code stolen from Django and django-oscar github repositories:

https://github.com/django/django/blob/main/django/utils/module_loading.py
https://github.com/django-oscar/django-oscar/blob/master/src/oscar/core/loading.py

"""

import sys
import traceback
from importlib import import_module


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError(
            'Module "%s" does not define a "%s" attribute/class'
            % (module_path, class_name)
        ) from err


def get_class(module_label, classname, module_prefix="backend.apps"):
    """
    Dynamically import a single class from the given module.

    This is a simple wrapper around `get_classes` for the case of loading a
    single class.

    Args:
        module_label (str): Module label comprising the app label and the
            module name, separated by a dot.  For example, 'catalogue.forms'.
        classname (str): Name of the class to be imported.

    Returns:
        The requested class object or `None` if it can't be found
    """
    return get_classes(module_label, [classname], module_prefix)[0]


def get_classes(module_label, classnames, module_prefix="backend.apps"):
    """
    Wrapper for the class loader
    """
    return class_loader(module_label, classnames, module_prefix)


def class_loader(module_label, classnames, module_prefix):
    """
    Dynamically import a list of classes from the given module.

    This works by looking up a matching app from the app registry,
    against the passed module label.  If the requested class can't be found in
    the matching module, then we attempt to import it from the corresponding
    core app.

    This is very similar to ``django.db.models.get_model`` function for
    dynamically loading models.  This function is more general though as it can
    load any class from the matching app, not just a model.

    Args:
        module_label (str): Module label comprising the app label and the
            module name, separated by a dot.  For example, 'catalogue.forms'.
        classname (str): Name of the class to be imported.

    Returns:
        The requested class object or ``None`` if it can't be found

    Examples:

        Load a single class:

        >>> get_class('showroom.views', 'Index')
        backend.apps.showroom.views.Index

        Load a list of classes:

        >>> get_classes('showroom.views',
        ...             ['Views', 'Components'])
        [backend.apps.showroom.views.Views
         backend.apps.showroom.views.Components]

    Raises:

        ImportError: If the attempted import of a class raises an
            ``ImportError``, it is re-raised
    """

    if "." not in module_label:
        # Importing from top-level modules is not supported, e.g.
        # get_class('shipping', 'Scale'). That should be easy to fix.
        # Overridable classes in a __init__.py might not be a good idea anyway.
        raise ValueError("Importing from top-level modules is not supported")

    # returns e.g. 'backend.apps.showroom.views.Index' or 'showroom.views.Index'
    # Attempt to import the classes from the app module
    app_module_label = ".".join([module_prefix, module_label])
    app_module = _import_module(app_module_label, classnames)

    # Attempt to import the classes from the generic module
    module = _import_module(module_label, classnames)

    if module is app_module is None:
        # This intentionally doesn't raise an ImportError, because ImportError
        # can get masked in complex circular import scenarios.
        raise ModuleNotFoundError(
            "The module with label '%s' could not be imported. This either"
            "means that it indeed does not exist, or you might have a problem"
            " with a circular import." % module_label
        )

    # return imported classes, giving preference to ones from the local package
    return _pluck_classes([app_module, module], classnames)


def _import_module(module_label, classnames):
    """
    Imports the module with the given name.
    Returns None if the module doesn't exist, but propagates any import errors.
    """
    try:
        return __import__(module_label, fromlist=classnames)
    except ImportError:
        # There are 2 reasons why there could be an ImportError:
        #
        #  1. Module does not exist. In that case, we ignore the import and
        #     return None
        #  2. Module exists but another ImportError occurred when trying to
        #     import the module. In that case, it is important to propagate the
        #     error.
        #
        # ImportError does not provide easy way to distinguish those two cases.
        # Fortunately, the traceback of the ImportError starts at __import__
        # statement. If the traceback has more than one frame, it means that
        # application was found and ImportError originates within the local app
        __, __, exc_traceback = sys.exc_info()
        frames = traceback.extract_tb(exc_traceback)
        if len(frames) > 1:
            raise


class ClassNotFoundError(Exception):
    """
    Exception for Not Found Class
    """


def _pluck_classes(modules, classnames):
    """
    Gets a list of class names and a list of modules to pick from.
    For each class name, will return the class from the first module that has a
    matching class.
    """
    klasses = []
    for classname in classnames:
        klass = None
        for module in modules:
            if hasattr(module, classname):
                klass = getattr(module, classname)
                break
        if not klass:
            packages = [m.__name__ for m in modules if m is not None]
            raise ClassNotFoundError(
                "No class '%s' found in %s" % (classname, ", ".join(packages))
            )
        klasses.append(klass)
    return klasses
