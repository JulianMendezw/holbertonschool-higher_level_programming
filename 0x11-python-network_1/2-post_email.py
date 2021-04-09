#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    (decoded in utf-8) """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url, email = argv[1], argv[2]
    header = {'email': email}
    data = parse.urlencode(header).encode('utf8')

    with request.urlopen(url, data=data) as response:
        print(response.read())
