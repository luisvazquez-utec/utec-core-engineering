#!/usr/bin/env python3
"""Accede a una secuencia por índice y gestiona los índices no válidos."""


def safe_index(sequence, index, default=None):
    """Devuelve el valor del índice o el valor predeterminado si está fuera
    de rango.
    """
    try:
        return sequence[index]
    except IndexError:
        return default
    except TypeError as error:
        message = "sequence must be indexable and index must be an integer"
        raise TypeError(message) from error


if __name__ == "__main__":
    print(safe_index(["Python", "exceptions"], 1))
