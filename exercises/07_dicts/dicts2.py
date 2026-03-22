# Topic: Dictionaries
# Exercise: dicts2

"""
Dictionary Methods

Useful dict methods:
    d.keys()              → all keys
    d.values()            → all values
    d.items()             → all (key, value) pairs
    d.get("key", default) → safe access (no KeyError)
    d.update({"x": 1})    → set multiple values at once

Safe access with .get():
    d = {"a": 1}
    d["b"]           → KeyError!
    d.get("b", 0)    → 0 (default value)

Your tasks:
1. Implement `invert(d)` → swaps keys and values
2. Implement `safe_add(d, key, value)` → adds value to d[key]
   (default value 0 if key doesn't exist, use .get())
3. Implement `filter_by_value(d, minimum)` → returns a new dict
   with only entries whose value >= minimum
"""


# ----- YOUR SOLUTION -----

def invert(d):
    # TODO: Return a new dict with {value: key for key, value in d.items()}
    pass


def safe_add(d, key, value):
    # TODO: d[key] = d.get(key, 0) + value; return d
    pass


def filter_by_value(d, minimum):
    # TODO: Return a new dict with entries where value >= minimum
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert({}) == {}

    d = {}
    safe_add(d, "points", 10)
    safe_add(d, "points", 5)
    assert d["points"] == 15, "d['points'] should be 15"

    prices = {"Apple": 0.5, "Banana": 1.2, "Kiwi": 0.8, "Pineapple": 3.0}
    expensive = filter_by_value(prices, 1.0)
    assert expensive == {"Banana": 1.2, "Pineapple": 3.0}, f"expensive → {expensive}"
    print("✓ dicts2 done!")
