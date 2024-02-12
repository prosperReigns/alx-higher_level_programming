#!/usr/bin/python3
"""A module for a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        if self.__height == 0:
            return 0
        elif self.__width == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
