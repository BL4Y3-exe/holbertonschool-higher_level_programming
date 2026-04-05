#!/usr/bin/python3
"""Module that defines Rectangle class."""


class Rectangle:
    """Represets a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if (self.__width == 0 or self.__height == 0):
            return 0
        return ((self.__width + self.__height) * 2)

    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles.
        """
        if not isinstance(rect_1, int):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, int):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ("")
        temp = ""
        for i in range(self.__height):
            if (i != 0):
                temp += "\n"
            temp += str(self.print_symbol) * self.__width
        return (temp)

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
