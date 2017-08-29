#!/usr/bin/python3
"""
search api
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv == 3):
        parameter = argv[2]
    else:
        parameter = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': argv[1]})

    try:
        response = r.json()
        if len(reponse.keys() == 0):
            print("No result")
        else:
            print("[{}] {}".format(reponse.get("id"), response.get("name")))
    except:
        print("Not a valid JSON")
