#!/usr/bin/python3
"""This module contains class_to_json function."""


def class_to_json(obj):
    """
    Function returns dict description of an instance of a class
    as json string.

    Args:
        obj: instance of a Class.

    Returns:
        str: the dictionary description with simple data structure."""
    return (obj.__dict__)
