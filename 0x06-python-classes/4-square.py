#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """a class Square that defines a square"""

    def __init__(self, size=0):
        self.__size = size

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")
