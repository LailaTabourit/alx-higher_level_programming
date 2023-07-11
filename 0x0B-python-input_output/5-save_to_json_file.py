#!/usr/bin/python3
""" Module that contains a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj: object
        filename: text file name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
