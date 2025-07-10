#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """
    This function retrieves a dictionary
    representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Module documented"""
    def to_json(self):
        return self.__dict__
