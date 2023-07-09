#!/usr/bin/python3
"""
9-student module - convert student to json
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """inistantination method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of student instance"""
        return vars(self)
