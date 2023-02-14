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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        if list_objs is None:
            list_objs = []
        dictionary_list = []
        for lst in list_objs:
            dictionary_list.append(lst.to_dictionary())
        json_string_list = Base.to_json_string(dictionary_list)
        with open("{:s}.json".format(cls.__name__), 'w+', encoding="utf-8")\
                as fp:
            fp.write(json_string_list)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
