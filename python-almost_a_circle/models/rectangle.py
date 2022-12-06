#!/usr/bin/python3
"""Rectangle class that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Define Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing method."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property Decorator."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Decorator."""
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property Decorator."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property."""

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """property decorator."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter Decorator."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property decorator."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter Decorator."""

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Area of a rectangle."""
        return self.width * self.height

    def display(self):
        """Display Function."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """returns [Rectangle]"""
         return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)
