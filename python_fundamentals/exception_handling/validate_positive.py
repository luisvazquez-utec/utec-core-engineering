#!/usr/bin/env python3
"""Validate that a value is a positive integer or float."""


def validate_positive(value):
    """Return a positive number; raise a specific error otherwise."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be an integer or float")
    if value <= 0:
        raise ValueError("value must be greater than zero")
    return value


if __name__ == "__main__":
    print(validate_positive(3))
