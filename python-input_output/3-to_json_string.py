#!/usr/bin/python3
"""This module contains to_json_string function."""
import json


def to_json_string(my_obj):
    """
    Function converts python object into json.

    Args:
        my_obj: object (string) to convert.

    Returns:
        JSON representation of an object.
    """
    return json.dumps(my_obj)
