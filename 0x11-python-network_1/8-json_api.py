#!/usr/bin/python3
"""
search api
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        parameter = argv[1]
    else:
        parameter = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': parameter})

    try:
        response = r.json()
        if len(response.keys()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except:
        print("Not a valid JSON")
