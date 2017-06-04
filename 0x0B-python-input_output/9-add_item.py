#!/usr/bin/python3
import sys


create_obj = __import__('8-load_from_json_file').load_from_json_file
save_obj = __import__('7-save_to_json_file').save_to_json_file

try:
    obj = create_obj("add_item.json")
except FileNotFoundError:
    obj = []

if (len(sys.argv) > 1):
    for i in range(1, len(sys.argv)):
        obj.append(sys.argv[i])

save_obj(obj, "add_item.json")
