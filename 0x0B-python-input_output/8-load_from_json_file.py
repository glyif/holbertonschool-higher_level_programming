#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a "JSON file"

    Args:
    @filename: JSON file to read from
    """
    with open(filename, mode='r') as fd:
        json_obj = fd.read()
        return (json.loads(json_obj))
