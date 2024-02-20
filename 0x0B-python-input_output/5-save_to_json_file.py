#!/usr/bin/python3
"""a module that conerts python object to json representation"""
import json
"""json module"""

def save_to_json_file(my_obj, filename):
    """writes to json file
    
    Args:
        my_obj (class): a python  object
        filename (str): path of file
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
