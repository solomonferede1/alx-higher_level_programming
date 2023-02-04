#!/usr/bin/python3
"""
The 1-write_file module - contains a function that writes a string
to file and returns no of chars written
"""


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
