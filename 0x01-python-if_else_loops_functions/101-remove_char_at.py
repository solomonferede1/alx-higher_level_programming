#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    new_str = ""
    for ch in str:
        if index == n:
            index += 1
            continue
        new_str += ch
        index += 1
    return new_str
