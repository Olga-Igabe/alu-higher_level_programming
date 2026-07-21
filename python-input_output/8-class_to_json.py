#!/usr/bin/python3
"""Module that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return a dictionary description of a simple-attribute object,
    suitable for JSON serialization."""
    return obj.__dict__
