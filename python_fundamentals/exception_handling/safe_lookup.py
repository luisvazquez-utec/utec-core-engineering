#!/usr/bin/env python3
"""Busca una clave e informa explícitamente si no existe."""


def safe_lookup(mapping, key):
    """Devuelve el valor de la clave o lanza una excepción descriptiva."""
    try:
        return mapping[key]
    except KeyError as error:
        raise KeyError("key not found: {!r}".format(key)) from error
    except TypeError as error:
        raise TypeError("mapping must support key lookup") from error


if __name__ == "__main__":
    print(safe_lookup({"language": "Python"}, "language"))
