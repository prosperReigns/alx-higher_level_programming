#!/usr/bin/python3
"""A module for a rectangle"""


class Rectangle:
    """represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """print a string representation of the object"""
        result = ''
        if self.__height == 0:
            return 0
        elif self.__width == 0:
            return 0
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(Rectangle.print_symbol)
            result += "\n"
        return result

    def __repr__(self):
        """print a string representation of the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance ot the rectangle object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __gt__(self, other):
        """comparison operation to determine the largest value
            between two instances
        """
        if not isinstance(other, Rectangle):
            raise TypeError("Cannot compare Rectangle \
                            with non-Rectangle object")
        return self.area() > other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """finds the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1 > rect_2:
            return rect_1
        elif rect_2 > rect_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """creates a new Rectangle instance"""
        return cls(size, size)
