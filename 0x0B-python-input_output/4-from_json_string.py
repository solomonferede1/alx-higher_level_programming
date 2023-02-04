#!/usr/bin/python3
"""
3-to_json_string module
change the json representaion to python data stracture
"""


import json


def from_json_string(my_str):
    """ Change to json string to python object"""
    return (json.loads(my_str))
