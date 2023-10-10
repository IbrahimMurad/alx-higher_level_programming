#!/usr/bin/python3
""" this is a script that adds all arguments to a Python list,
and then save them to a file
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
argv = __import__("sys").argv


save_to_json_file(argv[1:], "add_item.json")
