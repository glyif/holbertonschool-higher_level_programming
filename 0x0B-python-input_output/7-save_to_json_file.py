#!/usr/bin/python3


import json

def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    
    Args:
    @my_obj: object to a text file using json
    @filename: name of while to write in
    """
    with open(filename, mode='w') as fd:
        fd.write(json.dumps(my_obj))
