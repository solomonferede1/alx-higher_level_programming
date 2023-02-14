#!/usr/bin/python3
# Solomon Ferede - solomonf1227@gmail.com
"""
4-inherits_from module
check wether the object is an instance of a class that inherited from
the specified class
"""


def inherits_from(obj, a_class):
    """Function that returns true if an object is an instance of the class"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
