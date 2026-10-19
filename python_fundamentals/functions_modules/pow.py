#!/usr/bin/env python3


def pow(a, b):
    result = 1
    exponent = abs(b)

    for _ in range(exponent):
        result *= a

    if b < 0:
        return 1 / result
    return result
