#!/usr/bin/python3
"""a module that serialize a class"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a class"""
        return {"first_name": self.first_name, "last_name": self.last_name, "age": self.age}
