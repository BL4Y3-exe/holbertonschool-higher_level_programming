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
