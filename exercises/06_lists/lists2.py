# Topic: Lists
# Exercise: lists2

"""
List Methods

Lists have many useful methods:
    lst.append(x)      → Adds x at the end
    lst.pop()          → Removes and returns the last element
    lst.pop(i)         → Removes and returns element at index i
    lst.insert(i, x)   → Inserts x at position i
    lst.remove(x)      → Removes the first occurrence of x
    x in lst           → True if x is in the list
    lst.count(x)       → Number of occurrences of x

Your task:
Start with an empty list and perform the following operations:
1. Add 1, 2, 3 one at a time to the end
2. Insert 0 at position 0
3. Remove the last element
4. Remove the value 2 from the list
Result should be: [0, 1, 3]
"""


# ----- YOUR SOLUTION -----

stack = []

# TODO: Add 1, 2, 3 one at a time (append)

# TODO: Insert 0 at position 0 (insert)

# TODO: Remove the last element (pop)

# TODO: Remove the value 2 (remove)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert stack == [0, 1, 3], f"stack should be [0, 1, 3], but got {stack}"
    print("✓ lists2 done!")
