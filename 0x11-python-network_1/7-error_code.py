#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
    displays the body of the response. """
import requests
from sys import argv


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    code = response.statusstatus_code
    if code >= 400:
        print("Error code:", code)
    else:
        print(r.text)
