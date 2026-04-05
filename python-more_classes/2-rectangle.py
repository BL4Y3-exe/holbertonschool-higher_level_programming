#!/usr/bin/python3
"""Module that defines Rectangle class."""


class Rectangle:
    """Represets a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle.

        Args:
            width (int): The width of the ractangle.
            height (int): The height of the ractangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrives the width of rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the width of rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrives the height of rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets the width of rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The current area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimetr of the rectangle.

        Returns:
            int: The current perimetr of rectangle.
        """
        return ((self.__width + self.__height) * 2)
