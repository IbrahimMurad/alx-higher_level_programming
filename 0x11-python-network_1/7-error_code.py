#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code"""

import requests
import sys

if __name__ == "__main__":
    req = requests.post(sys.argv[1])
    if req.raise_for_status() is None:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
