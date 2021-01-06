#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """a class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if (len(position) is not 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """a class Square that defines a square"""
        return self.__size

    @size.setter
    def size(self, size):
        """a class Square that defines a square"""
        self.__size = size

        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """a class Square that defines a square"""
        return self.__position

    @position.setter
    def position(self, position):
        """a class Square that defines a square"""
        self.__position = position

    if (size < 0):
        raise ValueError("size must be >= 0")

    def my_print(self):
        """a class Square that defines a square"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end='')
                print("")
