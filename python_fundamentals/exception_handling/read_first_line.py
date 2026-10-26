#!/usr/bin/env python3
"""Lee la primera línea de un archivo y siempre lo cierra."""

import sys


def read_first_line(path):
    """Devuelve la primera línea sin el salto de línea final."""
    file_object = open(path, encoding="utf-8")
    try:
        return file_object.readline().rstrip("\n")
    finally:
        file_object.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: read_first_line.py <path>")
    print(read_first_line(sys.argv[1]))
