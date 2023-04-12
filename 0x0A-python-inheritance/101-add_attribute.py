#!/usr/bin/python3
"""
101-add_attribute module
Add attribute to an object if possible
"""


def add_attribute(obj, att_name, value):
    """Add attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, value)
