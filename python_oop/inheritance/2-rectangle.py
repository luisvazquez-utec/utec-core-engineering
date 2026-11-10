#!/usr/bin/env python3
"""Define a rectangle with area and string representation."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with positive dimensions."""

    def __init__(self, width, height):
        """Initialize the rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle's dimensions as a readable string."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
