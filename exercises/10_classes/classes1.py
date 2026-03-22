# Topic: Classes
# Exercise: classes1

"""
Defining Classes

A class is a blueprint for objects:
    class Dog:
        def __init__(self, name, breed):  # constructor
            self.name = name      # instance attribute
            self.breed = breed

        def bark(self):           # method
            return "Woof!"

    my_dog = Dog("Rex", "Labrador")
    my_dog.bark()  → "Woof!"

`self` always refers to the current object.

Your tasks:
1. Define the class `Rectangle` with:
   - `__init__(self, width, height)`
   - Method `area()` → returns width * height
   - Method `perimeter()` → returns 2 * (width + height)
   - Method `is_square()` → True if width == height
"""


# ----- YOUR SOLUTION -----

class Rectangle:
    def __init__(self, width, height):
        # TODO: Store width and height as self.width and self.height
        pass

    def area(self):
        # TODO: Return width * height
        pass

    def perimeter(self):
        # TODO: Return 2 * (width + height)
        pass

    def is_square(self):
        # TODO: True if width == height
        pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    r = Rectangle(4, 6)
    assert r.width == 4 and r.height == 6
    assert r.area() == 24, f"Area of 4x6 = 24, got: {r.area()}"
    assert r.perimeter() == 20, "Perimeter of 4x6 = 20"
    assert r.is_square() is False

    q = Rectangle(5, 5)
    assert q.area() == 25
    assert q.is_square() is True
    print("✓ classes1 done!")
