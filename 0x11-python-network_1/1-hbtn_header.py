#!/usr/bin/python3
"""
gets x-request-id from header
"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
