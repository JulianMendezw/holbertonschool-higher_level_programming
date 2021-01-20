#!/usr/bin/python3
""" Contain a class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """ This method print a string representation of the rectangle """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return str(self.__width * self.__height)
