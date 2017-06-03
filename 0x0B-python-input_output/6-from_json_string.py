#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object represented by a JSON string
    @my_str: string
    """
    return(json.loads(my_str))
