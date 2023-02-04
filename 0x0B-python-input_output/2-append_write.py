#!/usr/bin/python3
"""
The 2-append_file module - contains a function that appends
a string to file and returns no of chars written
"""


def append_write(filename="", text=""):
    """Append or Write on/to a file"""
    with open(filename, 'a+', encoding="utf-8") as f:
        return (f.write(text))
