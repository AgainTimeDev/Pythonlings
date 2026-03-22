# Topic: Classes
# Exercise: classes3

"""
Inheritance

With inheritance a class can extend another:
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "..."

    class Dog(Animal):
        def speak(self):        # override method
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

super() calls the parent class:
    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)  # parent constructor
            self.breed = breed

Your tasks:
The class `Shape` is given. Implement:
1. `Circle(Shape)` with `radius`, method `area()` = π * r²
2. `Square(Shape)` with `side`, method `area()` = side²
3. Both should set `name` via super().__init__()
"""


# ----- YOUR SOLUTION -----

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        # TODO: Call super().__init__("Circle") and store radius
        pass

    def area(self):
        # TODO: math.pi * radius ** 2
        pass


class Square(Shape):
    def __init__(self, side):
        # TODO: Call super().__init__("Square") and store side
        pass

    def area(self):
        # TODO: side ** 2
        pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    c = Circle(5)
    assert c.name == "Circle"
    assert abs(c.area() - math.pi * 25) < 0.001
    assert isinstance(c, Shape)

    s = Square(4)
    assert s.name == "Square"
    assert s.area() == 16
    assert isinstance(s, Shape)

    shapes = [Circle(3), Square(2)]
    for shape in shapes:
        assert callable(shape.area), "area() must be callable"
    print("✓ classes3 done!")
