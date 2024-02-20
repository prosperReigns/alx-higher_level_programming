#!/usr/bin/python3
"""a module that opens a file for reading"""


def read_file(filename=""):
    """read a file"""

    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
