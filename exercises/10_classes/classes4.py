# Topic: Classes
# Exercise: classes4

"""
Magic Methods (Dunder Methods)

Python classes can implement special methods:
    __str__   → str(obj) or print(obj)
    __repr__  → repr(obj), for developers
    __eq__    → obj1 == obj2
    __add__   → obj1 + obj2
    __len__   → len(obj)
    __abs__   → abs(obj)

Example:
    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __str__(self):
            return f"Point({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

Your task:
Implement the class `Vector`:
- `__init__(self, x, y)`
- `__str__` → "Vector(x, y)"
- `__repr__` → "Vector(x, y)"
- `__add__` → adds two vectors
- `__eq__` → compares two vectors (x and y equal)
- `__abs__` → returns the magnitude: sqrt(x² + y²)
"""


# ----- YOUR SOLUTION -----

import math

class Vector:
    def __init__(self, x, y):
        # TODO: Store x and y
        pass

    def __str__(self):
        # TODO: Return "Vector(x, y)"
        pass

    def __repr__(self):
        # TODO: Same as __str__
        pass

    def __add__(self, other):
        # TODO: Return new Vector(self.x + other.x, self.y + other.y)
        pass

    def __eq__(self, other):
        # TODO: True if self.x == other.x and self.y == other.y
        pass

    def __abs__(self):
        # TODO: math.sqrt(self.x**2 + self.y**2)
        pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    assert str(v1) == "Vector(3, 4)", f"str(v1) → {str(v1)!r}"
    assert repr(v2) == "Vector(1, 2)"

    v3 = v1 + v2
    assert v3 == Vector(4, 6), f"v1+v2 → {v3}"

    assert v1 == Vector(3, 4)
    assert v1 != v2

    assert abs(Vector(3, 4)) == 5.0, f"|v(3,4)| = 5.0, got: {abs(Vector(3,4))}"
    print("✓ classes4 done!")
