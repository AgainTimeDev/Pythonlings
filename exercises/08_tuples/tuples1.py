# Topic: Tuples
# Exercise: tuples1

"""
Tuple Basics

Tuples are like lists, but IMMUTABLE:
    point = (3, 7)
    point[0]    → 3
    point[0] = 5  → TypeError! (tuples are immutable)

A tuple with one element needs a comma:
    single = (42,)   # Without comma: just a number in parentheses

Tuple advantages:
- Faster than lists
- Can be used as dict keys
- Signal: "This data doesn't change"

Your tasks:
1. Create `coordinates` = tuple of (10, 20)
2. Create `color` = tuple of (255, 128, 0) – RGB
3. Create `single` = tuple with only one element: 42
4. Check: tuples are immutable (comment out the error line!)
"""


# ----- YOUR SOLUTION -----

coordinates = None  # TODO: Tuple (10, 20)

color = None        # TODO: Tuple (255, 128, 0)

single = None       # TODO: Tuple with only a 42 (don't forget the comma!)

# This code raises a TypeError – comment it out once you understand why!
coordinates_copy = (10, 20)
coordinates_copy[0] = 99  # This is intentionally wrong – comment out this line!

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert isinstance(coordinates, tuple), "coordinates must be a tuple"
    assert coordinates == (10, 20)
    assert color == (255, 128, 0)
    assert isinstance(single, tuple), "single must be a tuple"
    assert single == (42,), f"single should be (42,), but got {single!r}"
    print("✓ tuples1 done!")
