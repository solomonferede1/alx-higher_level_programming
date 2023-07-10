#!/usr/bin/python3
"""
100-append_after module
inserts a line of text to a file, after each line containing
a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line after a string containing line"""

    with open(filename, mode='r+', encoding='utf-8') as fp:
        all_lines = fp.readlines()
        fp.seek(0)
        for line in all_lines:
            fp.write(line)
            if search_string in line:
                fp.write(new_string)
        fp.truncate()
