#!/usr/bin/python3
"""a module that converts json string to python object"""
import json
"""json representation"""


def from_json_string(my_str):
    """converts json to pyhton object"""

    return json.loads(my_str)
