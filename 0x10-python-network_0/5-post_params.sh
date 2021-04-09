#!/bin/bash
# Post in URL and display the body
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
