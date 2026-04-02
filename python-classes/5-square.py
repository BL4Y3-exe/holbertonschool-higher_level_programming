#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """int: Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square using "#" simbol in stout."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
