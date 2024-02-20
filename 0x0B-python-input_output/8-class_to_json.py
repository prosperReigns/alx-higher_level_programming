#!/usr/bin/python3
"""a module that serialize an object"""


def class_to_json(obj):
    """returns a dictionary representation of an object"""
    return obj.__dict__
