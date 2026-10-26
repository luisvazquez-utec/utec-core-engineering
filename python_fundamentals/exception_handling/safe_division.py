#!/usr/bin/env python3
"""Divide dos valores y presenta errores de entrada de forma explícita."""


def safe_division(dividend, divisor):
    """Devuelve el cociente o lanza un error claro si los operandos
    no son válidos.
    """
    try:
        quotient = dividend / divisor
    except ZeroDivisionError as error:
        raise ValueError("divisor must not be zero") from error
    except TypeError as error:
        raise TypeError("both operands must support division") from error
    else:
        return quotient


if __name__ == "__main__":
    print(safe_division(10, 2))
