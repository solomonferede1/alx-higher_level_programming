#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if not (ord(ch) >= 65 and ord(ch) <= 90):
            ch = chr(ord(ch) + 32)
        print("{}".format(ch), end="")
    print()
    
