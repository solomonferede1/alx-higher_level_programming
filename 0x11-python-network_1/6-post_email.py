#!/usr/bin/python3
"""
2-post_email module
Post an email - urllib headers
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    Email = sys.argv[2]
    value = {'email': Email}

    resp = requests.post(url, parms=value)
    print(resp.text)
