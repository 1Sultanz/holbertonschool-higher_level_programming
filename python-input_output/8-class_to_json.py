#!/usr/bin/python3
"""Class to json"""

def class_to_json(obj):
    """This function reutrns the dictionary with simple data structure for JSON serialization of an object"""
    return obj.__dict__
