#!/usr/bin/env python3
def islower(c):
    """
    Devuelve True si c es una letra minúscula, False en caso contrario.
    Usa lógica ASCII con ord(), sin usar .islower()
    """
    # Validamos que sea un solo caracter
    if not isinstance(c, str) or len(c) != 1:
        return False
    # 'a' = 97, 'z' = 122 en ASCII
    return ord('a') <= ord(c) <= ord('z')
    # Equivalente a: return 97 <= ord(c) <= 122


# Pruebas
if __name__ == "__main__":
    print(islower('a'))  # True
    print(islower('A'))  # False
    print(islower('3'))  # False
    print(islower('z'))  # True
    print(islower('m'))  # True
    print(islower('Z'))  # False