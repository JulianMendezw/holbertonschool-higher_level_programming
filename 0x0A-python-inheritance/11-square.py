#!/usr/bin/python3
""" Contain a class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class Square that inherits from Rectangle (9-rectangle.py) """

    def __init__(self, size):
        """ Atributes of Square """

        self.__size = size
        self.integer_validator('size', size)

    def area(self):
        """ Area of a square """

        return self.__size ** 2

    def __str__(self):
        """ This is magic string """
        return ("[Square] {}/{}".format(self.__size, self.__size))
