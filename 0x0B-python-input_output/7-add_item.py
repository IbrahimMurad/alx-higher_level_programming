#!/usr/bin/python3
""" this is a script that adds all arguments to a Python list,
and then save them to a file
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
argv = __import__("sys").argv


try:
    to_add = load_from_json_file("add_item.json")
    to_add.extend(argv[1:])
    save_to_json_file(to_add, "add_item.json")
except:
    save_to_json_file(argv[1:], "add_item.json")
