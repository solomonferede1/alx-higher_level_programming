#!/usr/bin/python3
"""
8-json_api module
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        Q = ""       
    else:
        Q = sys.argv[1]

    r = requests.post(url, data={'q': Q})

    try:
        r_dict = r.json()
        if r_dict is not None:
            print('[{}] {}'.format(r_dict['id'], r_dict['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
