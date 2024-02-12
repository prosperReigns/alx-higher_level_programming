#!/usr/bin/python3
"""
    this module contains the add_integer function
    it uses two values a and b
    returns their sumation
"""


def add_integer(a, b=98):
    """
    add two numbers (int/float) together and output the sum of their sumation
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
