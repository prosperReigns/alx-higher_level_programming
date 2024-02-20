#!/usr/bin/python3
"""a module that appends a text to a file"""


def append_write(filename="", text=""):
    """appends text to file
    
    Args:
        filename (str): path to file
        text (str): text o be written
    Returns: number of characters read
    """

    with open(filename, "a", encoding="UTF-8") as file:
        char_read = file.write(text)
        return char_read
