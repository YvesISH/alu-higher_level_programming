#!/usr/bin/python3
"""contain the class BaseGeometry and SubClass rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """A representation of a square."""
    def __init__(self, size):
        """installation of the square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square."""
        return self.__size ** 2
