#!/usr/bin/python3
"""
The base module
"""


import json


class Base:
    """The base class for the rest of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class object with id number"""
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
