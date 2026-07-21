#!/usr/bin/python3
"""Module that checks if an object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherits from a_class, but is not
    a_class itself."""
    return isinstance(obj, a_class) and type(obj) is not a_class
