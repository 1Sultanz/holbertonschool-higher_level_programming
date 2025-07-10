#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) == a_class

