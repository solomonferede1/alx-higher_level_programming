#!/usr/bin/python3
# Post an email - urllib headers


from urllib import request
import sys


url = sys.argv[1]
Email = sys.argv[2]
headers = {'email': Email}

req = request.Request(url, None, headers)
with request.urlopen(req) as response:
    html = response.read()

html = html.decode('utf-8')
print(html)