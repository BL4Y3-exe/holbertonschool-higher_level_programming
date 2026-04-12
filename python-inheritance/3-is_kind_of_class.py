#!/usr/bin/python3
"""This module contains is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Function checks if the object is an instance of class
    or instance of its base class.

    Args:
        obj: object to check.
        a_class: specified class.
 
    Returns:
        True if the object is kind of class, False otherwise.
    """
    return (isinstance(obj, a_class))
