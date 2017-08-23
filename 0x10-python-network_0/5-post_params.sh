#/bin/bash
# post with parameters
curl -sL -X POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
