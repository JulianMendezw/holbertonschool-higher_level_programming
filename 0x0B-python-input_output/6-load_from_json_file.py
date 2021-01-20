#!/usr/bin/python3
""" A function that creates an Object from a “JSON file” """


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file” """
    with open(filename) as f:
        import json
        return json.load(f)
