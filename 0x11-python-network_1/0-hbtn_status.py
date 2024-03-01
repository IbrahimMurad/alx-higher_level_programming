#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    my_url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(my_url) as response:
        cont = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode()))
