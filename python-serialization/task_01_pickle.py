#!/usr/bin/python3
"""This module contains CustomObject class."""
import pickle

class CustomObject:
    """This class desribes a custom object.

    Attributes:
        name: name of object.
        age: age of object.
        is_student: status of object.

    Methods:
        display: prints all attributes of object.
        serialize: serializes instance and saves it in file.
        deserialize: creates new instance eith data in file.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Function prints all attributes of an instance."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Function serializes instance and saves it in file.

        Args:
            filename: path tp the file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Function creates new inctance with data in file.

        Args:
            filename: path to the file.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
