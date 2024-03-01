#!/usr/bin/python3
""" This module sends a request to a URL passed as an argument
and displays the value of the X-Request-Id variable found in the header of the response"""

import urllib.request, sys

if __name__ == "__main__":
    my_url = sys.argv[1]
    with urllib.request.urlopen(my_url) as response:
        val = response.getheader("X-Request-Id")
        print(val)
