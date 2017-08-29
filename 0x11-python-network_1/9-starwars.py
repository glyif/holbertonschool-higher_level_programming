#!/usr/bin/python3
"""
starwars api
"""

import requests
from sys import argv


if __name__ == "__main__":
    payload = {"search": argv[1]}
    r = requests.get("https://swapi.co/api/people", params=payload)

    response = r.json()

    count = response.get("count")

    print("Number of results: {}".format(count))

    results = response.get("results")

    if count > 0:
        for item in results:
            print(item.get("name"))
