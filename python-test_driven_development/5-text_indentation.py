#!/usr/bin/python3
"""
This module provides a function to print text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    text must be a string.
    Raises TypeError if not.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    new_line = True

    while i < len(text):
        char = text[i]

        if new_line and char == " ":
            i += 1
            continue

        print(char, end="")

        if char in ".?:":
            print("\n")
            new_line = True
        else:
            new_line = False

        i += 1
