#!/usr/bin/python3
"""
10-my_github module
Write Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(url, auth={username, token})
    r_dict = r.json()
    print('{}'.format(r_dict['id']))
