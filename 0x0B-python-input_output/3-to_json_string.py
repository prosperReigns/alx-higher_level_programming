#!/usr/bin/python3
"""a module that deserializes a string"""
import json
"""json representation"""


def to_json_string(my_obj):
    """converts python object to json string"""

    return json.dumps(my_obj)
