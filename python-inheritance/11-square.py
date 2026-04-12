#!/usr/bin/python3
"""This module contains Square class."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Args:
        Rectangle: base class.

    Attributes:
        __size: side size of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        Function calculates the area of square.

        Returns:
            int: the area of the square.
        """
        return (self.__size**2)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
