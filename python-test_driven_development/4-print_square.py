#!/usr/bin/python3
"""
This module provides a function to print a square using '#'.
"""


def print_square(size):
    """
    Prints a square of size 'size' using '#'.

    size must be an integer.
    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)