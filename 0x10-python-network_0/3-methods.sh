#!/bin/bash
# displays all methods

curl -si -X OPTIONS "$1" | grep "Allow: " | cut -d " " -f2-
