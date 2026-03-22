# Topic: Variables
# Exercise: variables4

"""
Augmented Assignment

Python offers convenient shorthand for arithmetic operations:
    x += 5   →  x = x + 5
    x -= 3   →  x = x - 3
    x *= 2   →  x = x * 2
    x //= 4  →  x = x // 4  (integer division)
    x **= 2  →  x = x ** 2  (power)
    x %= 3   →  x = x % 3   (modulo/remainder)

Your task: Follow the instructions and reach the target value!
"""


# ----- YOUR SOLUTION -----

points = 100

# TODO: Add 50 to points
# points = ???

# TODO: Subtract 30 from points
# points = ???

# TODO: Multiply points by 2
# points = ???

# TODO: Integer divide points by 4
# points = ???

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    # 100 + 50 = 150, 150 - 30 = 120, 120 * 2 = 240, 240 // 4 = 60
    assert points == 60, f"points should be 60, but got {points}"
    print("✓ variables4 done!")
