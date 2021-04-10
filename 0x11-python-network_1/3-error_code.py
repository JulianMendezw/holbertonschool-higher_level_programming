#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8). """
import urllib.request
from urllib.error import HTTPError
from sys import argv


try:
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf8')
        print(html)
except HTTPError as e:
    print('Error code:', e.code)
