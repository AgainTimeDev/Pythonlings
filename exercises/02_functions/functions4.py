# Topic: Functions
# Exercise: functions4

"""
*args and **kwargs

With *args a function accepts any number of positional arguments:
    def total(*numbers):
        return sum(numbers)
    total(1, 2, 3, 4)  → 10

With **kwargs a function accepts any number of keyword arguments:
    def info(**data):
        for key, value in data.items():
            print(f"{key}: {value}")
    info(name="Alice", age=30)

Your tasks:
1. Implement `total(*numbers)` → returns the sum of all numbers
   (Tip: use the built-in sum() function)
2. Implement `describe(**fields)` → returns a string:
   "key1=value1, key2=value2" (sorted by key)
"""


# ----- YOUR SOLUTION -----

def total(*numbers):
    # TODO: Return the sum of all numbers
    pass


def describe(**fields):
    # TODO: Return "key1=value1, key2=value2" (keys sorted alphabetically)
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert total(1, 2, 3) == 6
    assert total(10, 20, 30, 40) == 100
    assert total() == 0

    assert describe(name="Alice", age=30) == "age=30, name=Alice"
    assert describe(x=1) == "x=1"
    print("✓ functions4 done!")
