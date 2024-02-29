#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI $1 | grep -i "Allow:" | cut -f 2- -d " "
