#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/'
    url += sys.argv[1] + '/' + sys.argv[2] + '/commits?per_page=10'
    response = requests.get(url)
    com_list = response.json()
    for commit in com_list:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
