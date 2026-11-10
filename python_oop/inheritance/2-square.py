#!/usr/bin/env python3
"""Define a square with its own string representation."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a positive size."""

    def __init__(self, size):
        """Initialize the square with its validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square's dimensions as a readable string."""
        return "[Square] {}/{}".format(self.__size, self.__size)
