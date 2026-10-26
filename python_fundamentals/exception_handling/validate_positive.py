#!/usr/bin/env python3
"""Valida que un valor sea un entero o decimal positivo."""


def validate_positive(value):
    """Devuelve un número positivo o lanza una excepción específica."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be an integer or float")
    if value <= 0:
        raise ValueError("value must be greater than zero")
    return value


if __name__ == "__main__":
    print(validate_positive(3))
