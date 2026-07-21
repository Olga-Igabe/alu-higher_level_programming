#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception since area() must be implemented
        by subclasses."""
        raise Exception("area() is not implemented")
