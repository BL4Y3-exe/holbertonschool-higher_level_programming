#!/usr/bin/python3
"""This module contains BaseGeometry class."""


class BaseGeometry:
    """
    A BaseGeometry class.

    Methods:
        area: raises an exeption.
    """
    def area(self):
        """
        Public instance method.

        Raises:
            Exeption: area() is not implemented.
        """
        raise Exception("area() is not implemented")
