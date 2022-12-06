#!/usr/bin/python3
"""Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing method."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """A property decorator."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise Typ
