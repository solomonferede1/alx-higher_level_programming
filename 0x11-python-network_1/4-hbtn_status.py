#!/usr/bin/python3
"""
4-hbtn_status module
Fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    resp = requests.get(url)
    if resp.status_code == 200:
        print('Body response:')
        print('\t- type:', type(resp.text))
        print('\t- content:', resp.text)
