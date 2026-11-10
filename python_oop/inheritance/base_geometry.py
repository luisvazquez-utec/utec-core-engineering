#!/usr/bin/env python3
"""Define shared behavior for geometric shapes."""


class BaseGeometry:
    """Provide shared geometry methods and validation."""

    def area(self):
        """Raise an exception because the area is not defined here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
