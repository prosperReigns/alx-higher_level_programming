#!/usr/bin/python3
"""a module tat writes to a file"""


def write_file(filename="", text=""):
    """write a text to a file, creates it if it doesnt exist

    Args:
        filename (str): path of the file
        text (str): text to be written to file
    Returns: number of characyers written
    """

    with open(filename, "w", encoding="UTF-8") as file:
        char = file.write(text)
        return char
