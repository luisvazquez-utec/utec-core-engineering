#!/usr/bin/env python3
"""Convierte un valor a entero y muestra un error claro si no es válido."""


def parse_integer(value):
    """Devuelve el valor como entero o lanza ValueError si la entrada
    no es válida.
    """
    try:
        number = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError("value must be convertible to an integer") from error
    else:
        return number


if __name__ == "__main__":
    print(parse_integer("42"))
