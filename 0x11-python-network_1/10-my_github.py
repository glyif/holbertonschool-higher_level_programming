#!/usr/bin/python3
"""
github auth
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    try:
        url = 'https://api.github.com/user'
        r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
        print(r.json()['id'])
    except:
        print("None")
