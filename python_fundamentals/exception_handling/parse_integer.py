#!/usr/bin/env python3
"""Convert a value to an integer with a clear error message."""


def parse_integer(value):
    """Return value as an integer or raise ValueError for invalid input."""
    try:
        number = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError("value must be convertible to an integer") from error
    else:
        return number


if __name__ == "__main__":
    print(parse_integer("42"))
