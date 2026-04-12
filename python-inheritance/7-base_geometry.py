#!/usr/bin/python3
"""This module contains BaseGeometry class."""


class BaseGeometry:
    """
    A BaseGeometry class.

    Methods:
        area: raises an exeption.
        integer_validation: checkc if the value is in correct type and value.
    """
    def area(self):
        """
        Public instance method.

        Raises:
            Exeption: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function validates if value is in correct type and value.

        Args:
            name: name of smth.
            value: value of <name>.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal zero.
        """
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
