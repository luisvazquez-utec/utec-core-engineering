#!/usr/bin/env python3
"""Escribe una cadena UTF-8 en un archivo de texto."""


def write_file(filename="", text=""):
    """Escribe el texto en el archivo y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
