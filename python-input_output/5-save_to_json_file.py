#!/usr/bin/python3
"""This module contains save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to a text file,
    using a json representation.

    Args:
        my_obj: python object.
        filename: file to work with.
    """
    with open(filename, 'w', encoding="utf-8") as obj:
        json_str = json.dumps(my_obj)
        obj.write(json_str)
