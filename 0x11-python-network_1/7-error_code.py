#!/usr/bin/python3
"""
7-error_code module

determine and  display the error code
"""


if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    try:
        resp = requests.get(url)
        if resp.status_code < 400:
            print(resp.text)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("Error code:", err.args[0])
