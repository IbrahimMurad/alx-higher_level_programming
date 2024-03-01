#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""

from urllib import request, error
import sys


if __name__ == "__main__":
    req = request(sys.argv[1])
    try:
        response = request.urlopen(req)
        print(response.read().decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
