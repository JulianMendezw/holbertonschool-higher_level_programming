#!/usr/bin/python3
""" Contain a super class call Base """


class Base:
    """ Base class is the first class """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is not None:
            self.id = self.id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
