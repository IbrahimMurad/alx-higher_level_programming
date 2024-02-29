#!/bin/bash
# ends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -f -w '%{response_code}' -o /dev/null $1
