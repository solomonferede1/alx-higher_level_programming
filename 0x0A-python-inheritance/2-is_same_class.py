#!/usr/bin/python3
# Solomon Ferede - solomonf1227@gmail.com
"""
2-is_same_class module
check wether an object is instance of a specified class
"""


def is_same_class(obj, a_class):
    """Function that returns true if an object is an instance of the class"""
    return (type(obj) is a_class)
