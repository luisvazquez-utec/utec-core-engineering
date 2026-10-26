#!/usr/bin/env python3
"""Access a sequence by index while handling invalid indices."""


def safe_index(sequence, index, default=None):
    """Return the indexed value, or default when the index is out of range."""
    try:
        return sequence[index]
    except IndexError:
        return default
    except TypeError as error:
        message = "sequence must be indexable and index must be an integer"
        raise TypeError(message) from error


if __name__ == "__main__":
    print(safe_index(["Python", "exceptions"], 1))
