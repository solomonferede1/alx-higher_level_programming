#!/usr/bin/python3
"""
6-load_from_json_file module
It define a function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """ A method that creates an Object from a JSON file """

    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.loads(f.read())
