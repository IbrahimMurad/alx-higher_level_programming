#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    ses = requests.Session()
    ses.auth = (sys.argv[1], sys.argv[2])
    res = ses.get('https://api.github.com/user')
    print("{}".format(res.json()['id']))
