#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Represents a list with an additional print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))
