#!/usr/bin/python3
"""
6-load_from_json_file module
creates an Object a JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """creates an Object a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.loads(f.read())
