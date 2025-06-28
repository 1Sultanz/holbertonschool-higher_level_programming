#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
