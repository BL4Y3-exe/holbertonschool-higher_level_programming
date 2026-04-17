#!/usr/bin/python3
"""This module contains load_from_json_file function."""
import json


def load_from_json_file(filename):
    """
    Function creates an object from json file.

    Args:
        filename: file to work with.

    Returns:
        str: pyton object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.loads(json.read())
        return (obj)
