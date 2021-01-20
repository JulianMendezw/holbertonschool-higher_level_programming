#!/usr/bin/python3
""" a function that writes a string to a text file (UTF8) and
    returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Write a string to a text file (UTF8) """

    with open(filename, encoding="UTF-8", mode="w+") as f:
        return f.write(text)
