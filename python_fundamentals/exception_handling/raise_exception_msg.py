#!/usr/bin/env python3
"""Lanza una excepción NameError con un mensaje personalizado."""


def raise_exception_msg(message=""):
    """Lanza un NameError con el mensaje indicado."""
    raise NameError(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("This is a NameError")
    except NameError as error:
        print(error)
