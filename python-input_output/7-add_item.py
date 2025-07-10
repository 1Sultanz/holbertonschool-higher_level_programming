#!/usr/bin/python3
"""Save, add, load"""
import json


def save_to_json_file(my_obj, filename):
    """This function that writes an Object to a text file"""
    with open(filename, "w", encoding='utf-8') as f:
        a = json.dump(my_obj, f)
        return a

def load_from_json_file(filename):
    """A function that creates an Object from a json file"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)

my_list = [1, 2, 3, 4]
save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
