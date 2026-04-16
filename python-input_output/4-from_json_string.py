#!/usr/bin/python3
"""This module contains from_json_string function."""
import json


def from_json_string(my_str):
    """
    Function converts json string to python object.

    Args:
        my_str: json string to convert.

    Returns:
        an object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
