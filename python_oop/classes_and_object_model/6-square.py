#!/usr/bin/env python3
"""Define a Square class with a positioned string representation."""


class Square:
    """Represent a square with validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with its size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the square's position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square's position after validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or any(not isinstance(coordinate, int) or coordinate < 0
                   for coordinate in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using hash characters."""
        print(self)

    def __str__(self):
        """Return the square's shape, including its position."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        rows = (" " * x + "#" * self.__size for _ in range(self.__size))
        return "\n" * y + "\n".join(rows)
