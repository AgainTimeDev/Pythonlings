# Topic: Modules
# Exercise: modules2

"""
__name__ == "__main__"

When Python runs a file directly, __name__ == "__main__".
When the file is imported, __name__ is the module name.

This technique prevents code from running on import:
    def calculate(x):
        return x * 2

    if __name__ == "__main__":
        # Only runs when called directly, NOT when imported
        print(calculate(21))

This module has a PROBLEM: The code runs even when imported!

Your task:
Fix the file so that:
1. `double(x)` works and returns correct results
2. The print() call ONLY happens when run directly (inside __main__ guard)
3. The tests pass
"""


# ----- YOUR SOLUTION -----

def double(x):
    # TODO: This function should return x * 2
    pass

# This code has a problem: it runs ALWAYS, even when imported!
# TODO: Move the following code into an if __name__ == "__main__": block
print(f"Result: {double(21)}")


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert double(5) == 10
    assert double(0) == 0
    assert double(-3) == -6
    print("✓ modules2 done!")
