# Topic: Loops
# Exercise: loops3

"""
while loops

A while loop runs as long as a condition is True:
    while condition:
        # code

Example:
    n = 256
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    # steps == 8

Your tasks:
1. Implement `count_digits(n)` → returns the number of digits in a positive integer
   (without using str()!)
2. Implement `collatz_length(n)` → returns the length of the Collatz sequence:
   - if n is even: n = n // 2
   - if n is odd: n = 3 * n + 1
   - until n == 1
"""


# ----- YOUR SOLUTION -----

def count_digits(n):
    # TODO: Count digits with a while loop (divide by 10 until n == 0)
    if n == 0:
        return 1
    pass


def collatz_length(n):
    # TODO: Count the steps until n == 1
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert count_digits(1) == 1
    assert count_digits(9) == 1
    assert count_digits(10) == 2
    assert count_digits(999) == 3
    assert count_digits(1000) == 4

    assert collatz_length(1) == 1
    assert collatz_length(6) == 9, f"Collatz(6) has 9 steps, got: {collatz_length(6)}"
    assert collatz_length(27) == 112
    print("✓ loops3 done!")
