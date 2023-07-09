#!/usr/bin/python3
"""
The 8-class_to_json which converts object to json
"""
import json


def load_from_json_file(filename):
    """Convert to json"""

    with open(filename, "r", encoding="utf-8") as fp:
        return json.load(fp)
