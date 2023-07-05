#!/usr/bin/python3
"""

Module 0-add_integer
by: laila

"""


def add_integer(a, b=98):
    """ Function that adds 2 integers

    Args:
        a: first number
        b: second number

    Returns:
        addition of two numbers given

    Raises:
        TypesError: if a or b aren't integer and/or float numbers

    """

    if not sinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
