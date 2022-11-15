#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle
"""
Square class
"""


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ size init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Informal string that represent the square."""
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
