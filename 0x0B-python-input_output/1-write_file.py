#!/usr/bin/python3
""" Module contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """ Function that writes to a text file(UTF8)

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
