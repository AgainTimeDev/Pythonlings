# Topic: Variables
# Exercise: variables2

"""
Multiple Assignment and Variable Swapping

Python allows multiple assignment in one line:
    x, y = 10, 20

And elegant swapping without a temporary variable:
    x, y = y, x

Your tasks:
1. Assign x=10 and y=20 in one line
2. Swap x and y (without a temporary variable) in one line
3. Assign a, b, c the values 1, 2, 3
"""


# ----- YOUR SOLUTION -----

# TODO: Assign x=10 and y=20 in one line
x, y = None, None  # Replace None with the correct values

# Now swap:
# TODO: Swap x and y in one line

# TODO: Assign a=1, b=2, c=3 in one line
a, b, c = None, None, None

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert x == 20, f"x should be 20 after the swap, but got {x}"
    assert y == 10, f"y should be 10 after the swap, but got {y}"
    assert a == 1 and b == 2 and c == 3, f"a,b,c should be 1,2,3 but got {a},{b},{c}"
    print("✓ variables2 done!")
