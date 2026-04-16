#!/usr/bin/python3
"""This module contains append_file function."""


def append_write(filename="", text=""):
    """
    Function appends a string to the file.

    Args:
        filename: name of the file to work with.
        text: text to append.

    Returns:
        int: the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return (len(text))
