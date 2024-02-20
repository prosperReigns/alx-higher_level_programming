#!/usr/bin/python3
"""a module that coverts json to python object"""
import json
"""json module"""


def load_from_json_file(filename):
    """opens a json file in read mode and perform serialization"""

    with open(filename) as file:
        line = file.read()
        return json.loads(line)
