#!/usr/bin/python3
"""
0-add_integer module - define a function taht addes two integers
"""
def add_integer(a, b=98):
    """Define a function add_integert that add 2 int"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

