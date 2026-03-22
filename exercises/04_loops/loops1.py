# Topic: Loops
# Exercise: loops1

"""
for loop and range()

With range() you create number sequences:
    range(5)        → 0, 1, 2, 3, 4
    range(1, 6)     → 1, 2, 3, 4, 5
    range(0, 10, 2) → 0, 2, 4, 6, 8

for loops iterate over sequences:
    for i in range(5):
        print(i)

Your tasks:
1. Implement `sum_up_to(n)` → returns the sum 1+2+...+n
2. Implement `evens_up_to(n)` → returns a list of all even numbers from 0 to n
"""


# ----- YOUR SOLUTION -----

def sum_up_to(n):
    # TODO: Use a for loop with range() to compute 1+2+...+n
    pass


def evens_up_to(n):
    # TODO: Return a list of all even numbers from 0 to n (inclusive)
    # Tip: range(0, n+1, 2) generates even numbers
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert sum_up_to(5) == 15, f"1+2+3+4+5 = 15, got: {sum_up_to(5)}"
    assert sum_up_to(10) == 55
    assert sum_up_to(1) == 1
    assert sum_up_to(0) == 0

    assert evens_up_to(10) == [0, 2, 4, 6, 8, 10], f"evens_up_to(10) → {evens_up_to(10)}"
    assert evens_up_to(0) == [0]
    assert evens_up_to(7) == [0, 2, 4, 6]
    print("✓ loops1 done!")
