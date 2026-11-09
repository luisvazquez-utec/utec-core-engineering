# Classes and object model

This directory contains exercises for learning Python classes and objects.

## 0. My first square

`0-square.py` defines an empty `Square` class.

Example:

```python
Square = __import__("0-square").Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

The instance has no attributes, so its `__dict__` is `{}`.

## 1. Square with size

`1-square.py` defines a `Square` whose size is stored in the private instance
attribute `__size`.

Example:

```python
Square = __import__("1-square").Square

my_square = Square(3)
print(my_square.__dict__)
```

The instance dictionary contains `{'_Square__size': 3}`. The private attribute
is not available as `size` or `__size` through normal attribute access.

## 2. Size validation

`2-square.py` defaults the size to `0`, requires an integer, and rejects
negative values.

## 3. Square area

`3-square.py` adds the `area()` instance method, which returns the square of
the validated size.

## 4. Private size accessors

`4-square.py` exposes `size` through a property getter and setter. The setter
enforces the same integer and non-negative size rules used by earlier
exercises.

## 5. Print a square

`5-square.py` adds `my_print()` to print the square using `#` characters.
When the size is `0`, it prints an empty line.

## 6. Positioned square representation

`6-square.py` adds a validated `position` property and `__str__()` so printing
the instance renders its square with the requested spaces and leading lines.
`my_print()` uses the same representation.

## Rectangle: private dimensions

`1-rectangle.py` defines a `Rectangle` with validated private `width` and
`height` properties. Both dimensions default to `0` and must be non-negative
integers.

## Rectangle: area and perimeter

`2-rectangle.py` adds methods to calculate a rectangle's area and perimeter.
The perimeter is `0` whenever either dimension is `0`.
