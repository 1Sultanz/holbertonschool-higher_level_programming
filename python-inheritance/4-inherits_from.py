#!/usr/bin/python3
"""Defines an inheritance-checking function."""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class
    that inherited (directly or indirectly) from a_class.
    Return False if the object is an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
