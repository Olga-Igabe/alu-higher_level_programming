class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception since area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
