# Topic: Modules
# Exercise: modules1

"""
Importing Modules

Python has a huge standard library. Import modules like this:
    import math                    # Entire module
    from math import sqrt, pi      # Specific names
    from math import pi as PI      # With alias
    import statistics as stats     # Module with alias

Useful standard modules:
    math        → Mathematical functions (sqrt, sin, cos, pi, e, ...)
    random      → Random numbers (random(), randint(), choice(), shuffle())
    statistics  → Statistics (mean(), median(), stdev())
    os          → Operating system (getcwd(), path.join(), listdir())
    datetime    → Date and time

Your tasks:
1. Import math and compute `hypotenuse` = sqrt(3² + 4²)
2. Import pi from math as PI, compute `circle_area` = PI * 5²
3. Import statistics as stats, compute `mean` of [1,2,3,4,5,6,7,8,9,10]
"""


# ----- YOUR SOLUTION -----

# TODO: import math
# TODO: from math import pi as PI
# TODO: import statistics as stats

hypotenuse = None   # TODO: math.sqrt(3**2 + 4**2)

circle_area = None  # TODO: PI * 5**2

mean = None         # TODO: stats.mean([1,2,3,4,5,6,7,8,9,10])


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert abs(hypotenuse - 5.0) < 0.001, f"Hypotenuse(3,4) = 5.0, got: {hypotenuse}"
    assert abs(circle_area - 78.5398) < 0.01, f"Circle area r=5: {circle_area:.4f}"
    assert mean == 5.5, f"Mean(1..10) = 5.5, got: {mean}"
    print("✓ modules1 done!")
