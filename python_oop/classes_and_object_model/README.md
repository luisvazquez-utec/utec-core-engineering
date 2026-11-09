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
