# Topic: Conditions
# Exercise: if_else1

"""
Basic Conditionals (if/else)

With if and else you can execute code conditionally:
    if condition:
        # executed when condition is True
    else:
        # executed when condition is False

Comparison operators:
    ==  equal        !=  not equal
    <   less than    >   greater than
    <=  less or equal    >=  greater or equal

Your task:
Implement `classify(n)` that returns:
- "positive" when n > 0
- "negative" when n < 0
- "zero" when n == 0
"""


# ----- YOUR SOLUTION -----

def classify(n):
    # TODO: Return "positive", "negative", or "zero"
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert classify(5) == "positive", f"classify(5) → {classify(5)!r}"
    assert classify(-3) == "negative", f"classify(-3) → {classify(-3)!r}"
    assert classify(0) == "zero", f"classify(0) → {classify(0)!r}"
    assert classify(100) == "positive"
    assert classify(-0.1) == "negative"
    print("✓ if_else1 done!")
