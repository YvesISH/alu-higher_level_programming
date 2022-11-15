#!/usr/bin/python3
"""More class base"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """definition of a Rectangle."""
    def __init__(self, width, height):
        """Args: Constructor, Width and Height."""
        self.integer_validation("width", width)
        self.__width = width
        self.integer_validation("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
