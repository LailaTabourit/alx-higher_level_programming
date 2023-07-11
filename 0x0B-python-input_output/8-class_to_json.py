#!/usr/bin/python3
"""module that  returns the dictionary description"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    r = {}
    if hasattr(obj, "__dict__"):
        r = obj.__dict__.copy()
    return r
