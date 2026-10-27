#!/usr/bin/env python3
"""Añade una cadena UTF-8 al final de un archivo de texto."""


def append_write(filename="", text=""):
    """Añade el texto al archivo y devuelve los caracteres añadidos."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
