#!/usr/bin/python3
"""This module contains Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass of BaseGeometry.

    Args:
        BaseGeometry: a parent class.

    Attributes:
        __width: width of rectangle.
        __height: height of rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__height = height
        self.__width = width

    def area(self):
        """
        Function calculates the area of a rectangle.

        Returns:
            int: the are of rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
