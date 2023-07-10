#!/usr/bin/python3
"""
100-append_after module
inserts a line of text to a file, after each line containing
a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode='+a', encoding='utf-8') as fp:
        all_lines = fp.readlines()
        fp.seek(0)
        for line in all_lines:
            fp.writeline(line)
            if search_string in line:
                fp.writeline(new_string, '\n')
        fp.truncate()
