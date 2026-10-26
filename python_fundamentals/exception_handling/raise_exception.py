#!/usr/bin/env python3
"""Lanza una excepción de tipo TypeError."""


def raise_exception():
    """Lanza un TypeError con un mensaje explícito."""
    raise TypeError("This is a TypeError")


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as error:
        print(error)
