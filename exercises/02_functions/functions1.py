# Topic: Functions
# Exercise: functions1

"""
Defining Functions

With def you define a function:
    def greet(name):
        return "Hello, " + name + "!"

A function:
- starts with def
- has a name (by Python convention: lowercase_with_underscores)
- has optional parameters in ()
- contains indented code (4 spaces)
- returns a value with return

Your tasks:
1. Implement `greet(name)` → returns "Hello, {name}!"
2. Implement `square(n)` → returns n²
"""


# ----- YOUR SOLUTION -----

def greet(name):
    # TODO: Return "Hello, {name}!" (use an f-string or concatenation)
    pass


def square(n):
    # TODO: Return the square of n (n * n or n ** 2)
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert greet("World") == "Hello, World!", f"Expected 'Hello, World!', got: {greet('World')!r}"
    assert greet("Alice") == "Hello, Alice!", f"Expected 'Hello, Alice!', got: {greet('Alice')!r}"
    assert square(4) == 16, f"square(4) should be 16, but got {square(4)}"
    assert square(0) == 0, "square(0) should be 0"
    assert square(-3) == 9, "square(-3) should be 9"
    print("✓ functions1 done!")
