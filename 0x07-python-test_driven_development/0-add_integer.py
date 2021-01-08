#!/usr/bin/python3
"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers"""

    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')

    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')

    else:
        return int(a + b)
