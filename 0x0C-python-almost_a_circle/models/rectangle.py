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
        """gets and set the width of the rectangle
        
         Args:
            self (object): the object itself -> rectangle
            width (int): width of the recatangle
        """ 

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
        """gets and set the height of the rectangle
        
         Args:
            self (object): the object itself -> rectangle
            height (int): height of the recatangle
        """ 

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
        """gets and set the x cordinate
        
        Args:
            self (object): the object itself -> rectangle
            x (int): x cordinate of the recatangle
        """ 

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
        """gets and set the y cordinate
        
         Args:
            self (object): the object itself -> rectangle
            y (int): y cordinate of the recatangle
        """ 

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """finds the area of a rectangle"""

        return self.width * self.height


    def display(self):
        """ """
        for x in range(self.x):
            for y in range(self.y - 1):
                print("", end="\n")

        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print("", end="\n")


    def __str__(self):
        """ """
        return "[Rectangle] ({:d}) {:d}/{:d} -  {:d}/{:d}".format(self.id,
                                                                self.x, 
                                                                self.y,
                                                                self.width,
                                                                self.height)


    def update(self, *args, **kwargs):
        """ update th rectangle

        Args:
            self (object): the object itself -> rectangle
            args (tuple): variable number of arguments
            kwargs (dict): a key value pair
        """

        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width= args[1]
            if len(args) > 2:
                self.height= args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]


    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
