#!/usr/bin/python3
"""
8-json_api module
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[0]
    if sys.argv[1]:
        q = sys.argv[1]
    else:
        Q = ""

    val = {q: Q}
    r = requests.post(url, data=q)

    try:
        r_dict = r.json()
        if r_dict is not None:
            print('[{}] {}'.format(r_dict['id'], r_dict['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
