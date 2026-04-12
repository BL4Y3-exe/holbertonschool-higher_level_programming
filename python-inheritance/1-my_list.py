#!/usr/bin/python3
"""This module contains MyList class."""


class MyList(list):
    """
    This class is subclass of "list" class.

    Args:
        list: list class.

    Methods:
        print_sorted: prints a sorted version of list.
    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(self.sort())
