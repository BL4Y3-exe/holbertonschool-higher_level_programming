#!/usr/bin/python3
"""This module contains Student class."""


class Student:
    """
    This class defines Student.

    Attributes:
        first_name: the name of student.
        last_name: the last name of student.
        age: the age of student.

    Methods:
        to_json: retrieves a dictionary representation of a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function creates a dictionary of instance's attributes.

        Retunrs:
            dict: dictionary of the attributes.
        """
        dct =  {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

        if (attrs is None):
            return (dct)
        new_dct = {}
        for attr in attrs:
            if attr in dct.keys():
                new_dct[attr] = dct[attr]
        return (new_dct)
