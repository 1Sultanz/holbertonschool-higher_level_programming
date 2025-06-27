#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
