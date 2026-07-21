#!/usr/bin/python3
"""Module that defines a Student class with a filterable JSON export."""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names to include.
                If None, all attributes are included.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__
