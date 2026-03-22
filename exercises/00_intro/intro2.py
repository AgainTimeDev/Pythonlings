# Topic: Introduction
# Exercise: intro2

"""
Comments and Expressions

In Python, comments start with # (not // like in other languages).
Everything after # is ignored.

Your tasks:
1. Fix the comment on the line with "// This is not a Python comment"
2. Set `result` to the value of the expression 7 * 6
3. Set `greeting` to "Good Morning"
"""



# ----- YOUR SOLUTION -----

# This is not a Python comment - fix me!

result = None  # TODO: Calculate 7 * 6

greeting = None  # TODO: Set to "Good Morning"

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert result == 42, f"result should be 42, but got {result!r}"
    assert greeting == "Good Morning", f"greeting should be 'Good Morning', but got {greeting!r}"
    print("✓ intro2 done!")
