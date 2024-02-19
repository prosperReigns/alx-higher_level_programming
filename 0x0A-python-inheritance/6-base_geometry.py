#!/usr/bin/python3
"""executable file"""


class BaseGeometry:
    """a geometry class """
    def area(self):
        """calculate area of a geometry"""
        raise Exception("area() is not implemented")
