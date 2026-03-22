# Topic: Error Handling
# Exercise: error_handling1

"""
try/except – Basics

In Python you can catch errors:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        result = None

Common error types:
    ValueError        → Invalid value  (int("abc"))
    ZeroDivisionError → Division by zero
    TypeError         → Wrong type
    IndexError        → Index outside the list
    KeyError          → Key not in dict

Your tasks:
1. Implement `to_number(s)` → converts s to int, returns -1 on ValueError
2. Implement `safe_divide(a, b)` → divides a by b, returns 0 on ZeroDivisionError
"""


# ----- YOUR SOLUTION -----

def to_number(s):
    # TODO: Try int(s), catch ValueError and return -1
    pass


def safe_divide(a, b):
    # TODO: Try a / b, catch ZeroDivisionError and return 0.0
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert to_number("42") == 42
    assert to_number("-10") == -10
    assert to_number("abc") == -1, "Invalid string → -1"
    assert to_number("3.14") == -1, "Float string is not an int → -1"

    assert safe_divide(10, 2) == 5.0
    assert safe_divide(7, 0) == 0.0, "Division by zero → 0.0"
    assert safe_divide(0, 5) == 0.0
    print("✓ error_handling1 done!")
