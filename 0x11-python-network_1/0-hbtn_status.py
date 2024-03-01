#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print("Body response:")
    for header in response.headers:
        print("\t- {}".format(header))
