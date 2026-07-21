#!/usr/bin/python3
"""Module that defines the MyList class, a list subclass."""


class MyList(list):
    """A list subclass that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
