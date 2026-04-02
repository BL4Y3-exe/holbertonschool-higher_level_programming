#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): Position of the square (private).
    """

    def __init__(self, size=0, position=(0,0)):
        """Initialize a Square.

        Args:
            size (int): The size of the square.
            position (tuple): Position of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """tuple: Gets the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): Tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" *self.__size)
