# Topic: Lists
# Exercise: lists1

"""
List Basics

Lists store multiple values in a sequence:
    fruits = ["Apple", "Banana", "Cherry"]
    fruits[0]   → "Apple"   (first element)
    fruits[-1]  → "Cherry"  (last element)
    fruits[1] = "Mango"     (replace element)
    len(fruits) → 3         (length)

Lists can contain mixed types and are mutable.

Your tasks:
1. Create a list `numbers` with the values [10, 20, 30, 40, 50]
2. Assign `first` the first element
3. Assign `last` the last element (using a negative index)
4. Replace the third element (index 2) with 99
5. Assign `length` the length of the list
"""


# ----- YOUR SOLUTION -----

numbers = None  # TODO: List with [10, 20, 30, 40, 50]

first = None  # TODO: First element (index 0)

last = None   # TODO: Last element (negative index)

# TODO: Replace numbers[2] with 99
# numbers[???] = ???

length = None  # TODO: len(numbers)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert isinstance(numbers, list), "numbers must be a list"
    assert first == 10, f"first should be 10, but got {first}"
    assert last == 50, f"last should be 50, but got {last}"
    assert numbers[2] == 99, f"numbers[2] should be 99, but got {numbers[2]}"
    assert length == 5, f"length should be 5, but got {length}"
    print("✓ lists1 done!")
