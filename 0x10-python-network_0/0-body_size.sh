#/bin/bash
# gets length of response body
curl -si "$1" | grep "Content-Length:" | cut -d " " -f2
