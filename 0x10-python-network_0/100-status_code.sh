#!/bin/bash
# Send request to url and display the status code.
curl -so /dev/null -w "%{http_code}" "$1"
