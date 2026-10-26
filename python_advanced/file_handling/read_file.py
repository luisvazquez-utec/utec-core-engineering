#!/usr/bin/env python3
"""Lee un archivo de texto UTF-8 y muestra su contenido."""


def read_file(filename=""):
    """Imprime el contenido de un archivo de texto."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
