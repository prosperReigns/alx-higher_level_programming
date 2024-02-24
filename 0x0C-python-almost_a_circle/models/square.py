#1/usr/bin/python3
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
        """update the square
        
        Args:
            self (object): the object itself -> square
            args (tuple): size of the object
            kwargs (dict):
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    
    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }