#!/usr/bin/python3
"""Save, add, load"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = sys.argv[1:]
save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
