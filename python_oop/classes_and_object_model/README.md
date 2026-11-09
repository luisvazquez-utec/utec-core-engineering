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
