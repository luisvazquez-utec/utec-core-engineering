#!/usr/bin/env python3
"""Define a Square class with a private size and controlled access."""


class Square:
    """Represent a square with a validated private size."""

    def __init__(self, size=0):
        """Initialize the square with its size."""
        self.size = size

    @property
    def size(self):
        """Return the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
