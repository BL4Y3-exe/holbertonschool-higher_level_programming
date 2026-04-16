#!/usr/bin/python3
"""This module contain function to print text of a file."""


def read_file(filename=""):
    """
    Function prints text of a file.

    Args:
        filename: name of the file to print."""
    with open(filename, encoding="utf-8") as file:
        print(file.read())
