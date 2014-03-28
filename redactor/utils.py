from django.core.exceptions import ImproperlyConfigured
from django.utils import importlib


def import_class(path):
    path_bits = path.split('.')

    if len(path_bits) < 2:
        raise ImproperlyConfigured("'%s' is not a complete Python path." % path)

    class_name = path_bits.pop()
    module_path = '.'.join(path_bits)
    module_itself = importlib.import_module(module_path)

    if not hasattr(module_itself, class_name):
        raise ImportError("The Python module '%s' has no '%s' class." % (module_path, class_name))

    return getattr(module_itself, class_name)