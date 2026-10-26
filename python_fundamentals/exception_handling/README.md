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

- `safe_division.py`: distingue la división por cero de operandos incompatibles.
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

```sh
python3 safe_division.py
python3 read_first_line.py README.md
```

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
