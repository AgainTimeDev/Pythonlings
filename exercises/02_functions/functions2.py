# Topic: Functions
# Exercise: functions2

"""
Return Values

A function can return multiple values as a tuple with return:
    def min_max(numbers):
        return min(numbers), max(numbers)

    small, large = min_max([3, 1, 4, 1, 5])

Your tasks:
1. Implement `divide(a, b)` → returns quotient AND remainder (as a tuple)
   Use the // operator for integer division and % for the remainder.
2. Implement `is_even(n)` → returns True if n is even
"""


# ----- YOUR SOLUTION -----

def divide(a, b):
    # TODO: Return (quotient, remainder)
    # Example: divide(17, 5) → (3, 2)
    pass


def is_even(n):
    # TODO: Return True if n is even, otherwise False
    # Tip: n % 2 == 0 when n is even
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    quotient, remainder = divide(17, 5)
    assert quotient == 3, f"Quotient of 17/5 should be 3, but got {quotient}"
    assert remainder == 2, f"Remainder of 17/5 should be 2, but got {remainder}"

    q2, r2 = divide(10, 3)
    assert q2 == 3 and r2 == 1, f"10/3: expected (3,1), got ({q2},{r2})"

    assert is_even(4) is True, "4 is even"
    assert is_even(7) is False, "7 is odd"
    assert is_even(0) is True, "0 is even"
    print("✓ functions2 done!")
