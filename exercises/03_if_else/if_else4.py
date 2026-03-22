# Topic: Conditions
# Exercise: if_else4

"""
Ternary Expressions (Conditional Expressions)

Python has a compact syntax for simple if/else:
    value_if_true if condition else value_if_false

Examples:
    status = "adult" if age >= 18 else "minor"
    amount = number if number >= 0 else -number  # absolute value

Your tasks:
Write each TODO as a ONE-LINE ternary expression (not as an if/else block):
1. `sign`: "positive" if x > 0, otherwise "not positive"
2. `absolute`: the absolute value of x (without using abs())
3. `max_value`: the larger of a and b
"""


# ----- YOUR SOLUTION -----

x = -7
a = 15
b = 23

sign = None       # TODO: "positive" if x > 0, else "not positive" (ternary expression!)

absolute = None   # TODO: x if x >= 0, else -x (ternary expression!)

max_value = None  # TODO: a if a > b, else b (ternary expression!)


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert sign == "not positive", f"sign for {x} → {sign!r}"
    assert absolute == 7, f"absolute of {x} should be 7, but got {absolute}"
    assert max_value == 23, f"max({a}, {b}) should be 23, but got {max_value}"

    import inspect, ast
    src = inspect.getsource(inspect.getmodule(lambda: None))
    print("✓ if_else4 done!")
