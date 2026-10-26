#!/usr/bin/env python3
"""Imprime de forma segura los enteros de una lista."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime hasta x enteros y devuelve la cantidad impresa."""
    printed = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            continue
        printed += 1
    print()
    return printed
