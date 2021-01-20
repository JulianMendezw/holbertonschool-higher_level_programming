#!/usr/bin/python3
""" Contain a class BaseGeometry """


class BaseGeometry():
    """ class BaseGeometry """

    def area(self):
        """ That raises an Exception with the message """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate an integer value """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """Define an rectangle

        Args:
            BaseGeometry (class): Class BaseGeometry
    """

    def __init__(self, width, height):
        """ Atributtes of the class Rectangule """
        self.__width = width
        self.__height = height

        self.integer_validator('width', width)
        self.integer_validator('height', height)
