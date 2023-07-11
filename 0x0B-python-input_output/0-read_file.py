#!/usr/bin/python3
""" function reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened or it doesn't exist

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
