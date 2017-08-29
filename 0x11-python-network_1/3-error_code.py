#!/usr/bin/python3
"""
error handling
"""

import urllib.request
import urllib.HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with url.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e))