#!/usr/bin/env python3


def uppercase(str):
    result = ""
    for character in str:
        code = ord(character)
        if ord('a') <= code <= ord('z'):
            code -= 32
        result += "{:c}".format(code)
    print(result)
