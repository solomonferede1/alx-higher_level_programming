#!/usr/bin/python3
"""
7-error_code module

determine and  display the error code
"""


if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    resp = requests.get(url)
    if resp.ok is False:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
