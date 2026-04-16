#!/usr/bin/python3
"""This module contains write_file function."""


def write_file(filename="", text=""):
    """
    Function overwrite the content of the file.

    Args:
        filename: name of the file to work with.
        text: text to write.

    Returns:
        int: the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return (len(text))
