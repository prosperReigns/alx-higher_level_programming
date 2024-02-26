#!/usr/bin/python3
"""a module that creates a square from a rectangle"""
from models.rectangle import Rectangle
"""importing subclass rectangle"""


class Square(Rectangle):
    """ a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square

        Args:
            size (int): size of the square
            x (int): cordinate x of the square
            y (int): cordinate y of the square
            id (int): identity of the object - __nb_objects
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints a string representation of an object"""
        return "[Square] ({:d}) {:d}/{:d} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """get and set the size of an object

        Args:
            self (object): the object itself -> square
            value (int): size of the object
        """

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be >= 0")

        self.__size = size

    def update(self, *args, **kwargs):
        """Update the Square

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """converts an instance into a python string"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
