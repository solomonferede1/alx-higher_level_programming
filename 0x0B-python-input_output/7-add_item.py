#!/usr/bin/python3
"""
7-add_item module
contains a function that adds all arguments to a Python list, and
then save them to a file:
"""


import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def create_file_list():
    """Adds all arguments to a Python list, and then save them to a file"""
    obj_9 = load_from_json_file("add_item.json")

    for i in range(1, len(sys.argv)):
        obj_9.append(str(sys.argv[i]))

    save_to_json_file(obj_9, "add_item.json")
