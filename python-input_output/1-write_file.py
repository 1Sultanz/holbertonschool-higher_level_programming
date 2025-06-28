#!/usr/bin/python3
"""
This module provides a function to write a string to a text file (UTF8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns
    the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
