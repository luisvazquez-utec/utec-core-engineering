#!/usr/bin/env python3
"""Imprime de forma segura una cantidad de elementos de una lista."""


def safe_print_list(my_list=[], x=0):
    """Imprime hasta x elementos y devuelve cuántos pudo imprimir."""
    printed = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
        except IndexError:
            break
        printed += 1
    print()
    return printed
