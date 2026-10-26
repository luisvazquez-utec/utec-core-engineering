#!/usr/bin/env python3
"""Look up a key and report missing keys explicitly."""


def safe_lookup(mapping, key):
    """Return the value for key or raise a descriptive exception."""
    try:
        return mapping[key]
    except KeyError as error:
        raise KeyError("key not found: {!r}".format(key)) from error
    except TypeError as error:
        raise TypeError("mapping must support key lookup") from error


if __name__ == "__main__":
    print(safe_lookup({"language": "Python"}, "language"))
