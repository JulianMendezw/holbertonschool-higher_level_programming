#!/usr/bin/python3
""" Contain a super class call Base """


class Base:
    """ Base class is the first class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to a json string """

        import json
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of dictionaries to a file """

        if list_objs is None:
            new_list = []

        else:
            new_list = []
            for objects in list_objs:
                new_list.append(cls.to_dictionary(objects))
            new_list = Base.to_json_string(new_list)

        with open("{}.json".format(cls.__name__), 'w') as f:
            import json
            new_list = Base.to_json_string(new_list)
            f.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list from the JSON string representation """

        if json_string is None or not json_string:
            return []

        import json
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance and update it with a dictionary """

        x = 1 if cls.__name__ == 'Rectangle' else 0

        dummy = cls(1, x)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from JSON file """

        try:
            with open("{}.json".format(cls.__name__)) as f:

                json_list = Base.from_json_string(f.read())
                instances_list = []

                for dictionary in json_list:
                    instances_list.append(cls.create(**dictionary))
                return instances_list

        except Exception:
            return []
