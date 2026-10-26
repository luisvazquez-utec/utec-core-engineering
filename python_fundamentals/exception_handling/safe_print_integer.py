#!/usr/bin/env python3
"""Imprime un entero de forma segura."""


def safe_print_integer(value):
    """Imprime value como entero y devuelve True si tiene formato válido."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
