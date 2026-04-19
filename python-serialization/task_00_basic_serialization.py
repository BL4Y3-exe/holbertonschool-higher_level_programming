#!/usr/bin/python3
"""
This module contains serialize_and_save_to_file and
load_and_deserialize functions.
"""
import json

def serialize_and_save_to_file(data, filename):
    """
    Fucntion serializes a Python dictionary into json format
    and saves it to file.

    Args:
        data: A Python Dictionary with data.
        filename: The filename of the output JSON file.
    """
    with open(filename, 'w', encoding="utf-8") as pyf:
        json.dump(data, pyf)

def load_and_deserialize(filename):
    """
    Function loads json data from a file and converts it
    back into a Python dictionary.

    Args: 
        filename: The filename of the input JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as jsonf:
        return json.load(jsonf)
