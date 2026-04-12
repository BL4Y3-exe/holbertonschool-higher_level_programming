#!/usr/bin/python3
"""This module contains inherits_from function."""


def inherits_from(obj, a_class):
    """
    Function checks if the object is an instance of class
    that inherited from the specified class.

    Args:
        obj: object to check.
        a_class: specified class.

    Returns:
        True if the object fits the conditions, False otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
