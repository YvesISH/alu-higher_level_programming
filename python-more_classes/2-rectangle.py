#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Define aa class Rectangle."""
    def __init__(self, width=0, height=0):
        """Initializing
            Args: height & width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set Height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a Rectangle"""
        return (self.__width * self.__height)

    def perimiter(self):
        """Return Perimiter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
