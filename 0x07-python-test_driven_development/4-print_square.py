#!/usr/bin/python3
""""draws a square of size (int) """


def print_square(size):
    """
    prints a square of a desired size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for i in range(size):
            print("#", end="")
        print("", end="\n")
