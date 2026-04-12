#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This module contains abstract class Animal, and its subclasses Dog and Cat.
"""


class Animal(ABC):
    """
    An abstract Animal class.

    Args:
        ABC: an abstract class definer
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Class that describes Dog.

    Args:
        Animal: parent class.
    """
    def sound(self):
        """
        Function returns sound for dog.

        Returns:
            string: "Bark".
        """
        return ("Bark")


class Cat(Animal):
    """
    Class that describes Cat.

    Args:
        Animal: parent class.
    """
    def sound(self):
        """
        Function returns sound for cat.

        Returns:
            string: "Meow".
        """
        return ("Meow")
