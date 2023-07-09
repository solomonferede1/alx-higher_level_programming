#!/usr/bin/python3
"""
The 8-class_to_json which converts object to json
"""
import json


def class_to_json(obj):
    """Convert to json"""

    return vars(obj)
