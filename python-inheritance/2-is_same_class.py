#!/usr/bin/python3
"""This module contains is_same_class function."""


def is_same_class(obj, a_class):
    """
    Function checks if the object is an instance of the specified class.

    Args:
        obj: an instance of a some class.
        a_class: a particular class.

    Returns:
        bool: True if obj is exactly an instance of the a_class,
        False otherwise.
    """
    return (type(obj) is a_class)
