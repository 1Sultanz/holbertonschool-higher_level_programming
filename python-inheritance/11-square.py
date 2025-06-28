#!/usr/bin/python3
"""Square class that inherits from Rectangle (based on 10-square.py)."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
