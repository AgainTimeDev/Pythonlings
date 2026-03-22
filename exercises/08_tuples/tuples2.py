# Topic: Tuples
# Exercise: tuples2

"""
Tuple Unpacking

You can "unpack" tuples directly into variables:
    x, y = (3, 7)
    name, age, city = ("Alice", 30, "Berlin")

With * you can collect the rest:
    first, *rest = (1, 2, 3, 4, 5)
    # first = 1, rest = [2, 3, 4, 5]

    *start, last = (1, 2, 3, 4, 5)
    # start = [1, 2, 3, 4], last = 5

Your tasks:
1. Unpack `person` into `name`, `age`, `profession`
2. Unpack `numbers` as: `first`, `*middle`, `last`
3. Implement `min_max(lst)` → returns (minimum, maximum)
"""


# ----- YOUR SOLUTION -----

person = ("Alice", 28, "Developer")
numbers = (1, 2, 3, 4, 5, 6, 7)

# TODO: Unpack person into name, age, profession
name = None
age = None
profession = None
# name, age, profession = ???

# TODO: Unpack numbers into first, *middle, last
first = None
middle = None
last = None
# first, *middle, last = ???


def min_max(lst):
    # TODO: Return (min(lst), max(lst))
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert name == "Alice" and age == 28 and profession == "Developer"
    assert first == 1
    assert middle == [2, 3, 4, 5, 6], f"middle → {middle}"
    assert last == 7

    small, large = min_max([3, 1, 4, 1, 5, 9, 2, 6])
    assert small == 1 and large == 9
    print("✓ tuples2 done!")
