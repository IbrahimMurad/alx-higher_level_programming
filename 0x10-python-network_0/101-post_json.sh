#!/bin/bash
# ends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -X POST -json "@$2" "$1"