#!/bin/bash
# Display all HTPPS methods the server will accept
curl -sI "$1" | grep "Allow" | sed -ne 's/^Allow: //p'
