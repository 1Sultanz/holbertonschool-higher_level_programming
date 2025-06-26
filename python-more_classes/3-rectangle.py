#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            return "\n".join(["#" * self.__width for _ in range(
                self.__height)])


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(
        my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
