#!/usr/bin/python3
"""a module for a base class"""


class Base:
    """a base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        self.id= id

        if (self.id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
