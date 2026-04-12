#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
This module contains abstract class Shape, and Circle, Rectangle subclasses.
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class.

    Args:
        Shape: parent class.

    Methods:
        area: returns the area of circle.
        perimeter: return the perimeter of circle.
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """
        Calculates the area of circle.

        Returns:
            int: the area of circle.
        """
        return (pi * self.radius**2)
    
    def perimeter(self):
        """
        Calculates the perimeter of circle.

        Returns:
            int: the perimemter of circle.
        """
        return (2 * pi * self.radius)
    


class Rectangle(Shape):
    """
    Rectangle class.

    Args:
        Shape: parent class.

    Methods:
        area: returns the area of rectangle.
        perimeter: returns the perimeter of rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of object.

        Returns:
            int: the area of rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculates the perimeter of rectangle.

        Returns:
            int: the perimeter of rectangle.
        """
        return ((self.width + self.height) * 2)


def shape_info(obj):
    """
    Function prints information about an instance.

    Args:
        obj: any subclass of Shape.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
