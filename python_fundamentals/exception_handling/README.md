# Manejo de excepciones en Python

Los errores en tiempo de ejecución pueden deberse a entradas inválidas, datos
faltantes u operaciones que no se pueden completar. Las excepciones permiten
detectar estas situaciones y decidir cómo responder sin ocultar errores
inesperados.

## Objetivos de aprendizaje

- Reconocer `TypeError`, `IndexError`, `ZeroDivisionError` y `KeyError`.
- Capturar excepciones específicas con `try` y `except`.
- Usar `else` para el código que solo debe ejecutarse cuando no hay errores.
- Usar `finally` para garantizar la limpieza de recursos.
- Lanzar excepciones explícitamente con `raise`.
- Escribir funciones con errores previsibles y documentados.

## Ejercicios

- `safe_print_integer.py`: imprime un valor con formato entero y devuelve
  `False` si no se puede representar como entero.
- `safe_print_list_integers.py`: imprime solo los enteros de los primeros
  `x` elementos y devuelve cuántos imprimió. Si `x` supera el tamaño de la
  lista, propaga `IndexError`.
- `safe_print_list.py`: imprime hasta una cantidad indicada de elementos sin
  usar `len()` y maneja el fin de la lista con `try` y `except`.
- `safe_division.py`: distingue la división por cero de operandos incompatibles.
- `raise_exception.py` y `raise_exception_msg.py`: lanzan excepciones explícitas
  con mensajes fijos o personalizados.
- `safe_lookup.py`: comunica claramente una clave ausente o un objeto no
  indexable como diccionario.
- `safe_index.py`: maneja índices fuera de rango y valida el tipo de índice.
- `parse_integer.py`: convierte valores a enteros y comunica entradas inválidas.
- `validate_positive.py`: valida el tipo y el rango de un número, lanzando
  excepciones específicas.
- `read_first_line.py`: usa `finally` para cerrar un archivo incluso si la
  lectura falla.

Cada archivo incluye una función que se puede importar y una demostración
ejecutable. Por ejemplo:

Desde la carpeta `python_fundamentals/exception_handling`:

```sh
python3 safe_division.py
python3 read_first_line.py README.md
```

Desde la raíz del repositorio, usa la ruta relativa de la carpeta:

```sh
python3 python_fundamentals/exception_handling/safe_division.py
python3 python_fundamentals/exception_handling/read_first_line.py python_fundamentals/exception_handling/README.md
```

Para probar `safe_print_list` interactivamente desde la raíz, inicia Python e
importa la función antes de llamarla:

```pycon
>>> from python_fundamentals.exception_handling.safe_print_list import safe_print_list
>>> mi_lista = [10, 20, 30]
>>> resultado = safe_print_list(mi_lista, 5)
102030
>>> print("resultado:", resultado)
resultado: 3
```

En PowerShell, escribe primero `py -3` para abrir el intérprete de Python. Las
asignaciones y llamadas de Python se escriben después del indicador `>>>`, no
directamente en el indicador `PS>`.

## `else` y `finally`

El bloque `else` de `try` se ejecuta solo si el bloque `try` termina sin
excepciones. `finally` se ejecuta tanto si ocurre una excepción como si no,
por lo que es apropiado para liberar recursos:

```python
try:
    result = int(value)
except (TypeError, ValueError) as error:
    raise ValueError("Se esperaba un entero válido") from error
else:
    print("Conversión correcta:", result)
finally:
    print("Conversión finalizada")
```

## Requisitos

- Python 3.8.x.
- Ubuntu 20.04 LTS para la corrección.
- Sin bibliotecas externas.
- Los archivos Python comienzan con `#!/usr/bin/env python3`, terminan con
  una nueva línea y siguen PEP 8 (pycodestyle 2.7.x).
