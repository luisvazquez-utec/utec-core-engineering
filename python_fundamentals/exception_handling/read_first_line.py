#!/usr/bin/env python3
"""Read the first line of a file and always close the file."""

import sys


def read_first_line(path):
    """Return the first line without its trailing newline."""
    file_object = open(path, encoding="utf-8")
    try:
        return file_object.readline().rstrip("\n")
    finally:
        file_object.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: read_first_line.py <path>")
    print(read_first_line(sys.argv[1]))
