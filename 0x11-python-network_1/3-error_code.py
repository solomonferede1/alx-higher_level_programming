#!/usr/bin/python3
"""
3-error_code.py module
handle errors in http request using python
"""


from urllib import request
from urllib.error import HTTPError, URLError
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            html = response.read()
        html = html.decode('utf-8')
        print(html)
    except HTTPError as e:
        print("Error code:", e.code)
