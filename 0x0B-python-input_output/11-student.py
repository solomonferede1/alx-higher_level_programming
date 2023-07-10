#!/usr/bin/python3
"""
The 10-student module
Student to JSON with filter
"""


class Student:
    """Define a student"""

    def __init__(self, first_name, last_name, age):
        """nstantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves json representation of student instanse"""
        if isinstance(attrs, list):
            filt_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    filt_dict[key] = value
            return filt_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
