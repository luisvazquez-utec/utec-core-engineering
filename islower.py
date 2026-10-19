#!/usr/bin/env python3


def islower(c):
    """Return True if c is a lowercase ASCII letter."""
    if not isinstance(c, str) or len(c) != 1:
        return False

    return ord('a') <= ord(c) <= ord('z')


if __name__ == "__main__":
    for character in (' ', 'a', 'H', '4', '!', 4):
        print(islower(character))
