#!/usr/bin/python3
"""This module contains function for lookup."""


def lookup(obj):
    """
    This function prints all attributes and methods of a given object.

    Arguments:
        obj: an object.

    Return:
        list: Returns a list object.
    """
    return (dir(obj))
