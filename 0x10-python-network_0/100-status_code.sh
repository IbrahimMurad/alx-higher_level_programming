#!/bin/bash
# ends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -I -w '%{response_code}' -no-head $1
