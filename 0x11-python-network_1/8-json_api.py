#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
    - The letter must be sent in the variable q
    - If no argument is given, set q=""
    - If the response body is properly JSON formatted and not empty,
        display the id and name like this: [<id>] <name>
        Otherwise:
            = Display Not a valid JSON if the JSON is invalid
            = Display No result if the JSON is empty"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        parameters = {'q': sys.argv[1]}
    else:
        parameters = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data=parameters)
    try:
        json = eval(req.text)
        if type(json) is dict:
            if len(json) > 0:
                print("[{}] {}".format(json['id'], json['name']))
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except Exception:
        print("Not a valid JSON")
