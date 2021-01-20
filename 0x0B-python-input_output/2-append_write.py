#!/usr/bin/python3
""" A function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file (UTF8) """

    with open(filename, encoding="UTF-8", mode="a") as f:
        return f.write(text)
