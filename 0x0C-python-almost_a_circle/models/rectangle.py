#!/usr/bin/python3
""" a module that inherit from a base"""

from models.base import Base


class Rectangle(Base):
    """dimension of rectangle - size of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """gets and set the width of te rectangle""" 

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """gets and set the height of the rectangle""" 

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """gets and set the x cordinate""" 

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """gets and set the y cordinate""" 

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """finds the area of a rectangle"""

        return self.width * self.height

    def display(self):
        for x in range(self.x):
            for y in range(self.y - 1):
                print("", end="\n")
            # print("", end="\n")

        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print("", end="\n")

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)