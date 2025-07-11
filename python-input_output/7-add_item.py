#!/usr/bin/python3
"""Save, add, load"""
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = [1, 2, 3, 4]
save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
