#!/usr/bin/python3
""" a class Student that defines a student by """


class Student:
    """ a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for i, j in self.__dict__.items():
            if i in attrs:
                new_dict[i] = j

        return new_dict
