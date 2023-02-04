#!/usr/bin/python3
"""
The 0-read_file module - contains a function that reads file and prints to stdout
"""


def read_file(filename=""):
    """A function reads txt from the file"""
    with open('filename', 'r', encoding="UTF-8") as f:
        print(f,read())
