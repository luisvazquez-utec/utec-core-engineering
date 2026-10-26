#!/usr/bin/env python3
"""Divide dos valores e muestra el resultado incluso si ocurre un error."""


def safe_print_division(a, b):
    """Devuelve la división o None si ocurre una excepción."""
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
