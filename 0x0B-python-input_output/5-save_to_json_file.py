#!/usr/bin/python3
""" A function that writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file """

    with open(filename, 'w+') as f:
        import json
        f.write(json.dumps(my_obj))
