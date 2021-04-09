#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the response. """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf8')))
