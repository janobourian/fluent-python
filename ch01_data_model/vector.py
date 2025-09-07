"""
Vector class represents a 2D vector with x and y components.

It is simplistic for didatic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mukti__`` methods.

This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
    
Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Scala multiplication::

    >>> v = Vector(3, 4)
    >>> v * 3
    Vector(9, 12)
    
Boolean value::

    >>> bool(Vector(0, 0))
    False
    >>> bool(Vector(1, 1))
    True
"""
import math

class Vector:
    
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: int | float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)