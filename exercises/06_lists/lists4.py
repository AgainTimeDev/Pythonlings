# Topic: Lists
# Exercise: lists4

"""
Sorting

Python offers two ways to sort:
    sorted(lst)         → returns a NEW sorted list (original unchanged)
    lst.sort()          → sorts the list IN-PLACE

With the key parameter you can customize the sort logic:
    sorted(words, key=len)                     → by word length
    sorted(words, key=str.lower)               → ignore case
    sorted(people, key=lambda p: p["age"])     → by age

With reverse=True you sort in descending order:
    sorted([3,1,2], reverse=True)  → [3, 2, 1]

Your tasks:
1. Sort `words` by word length (shortest first)
2. Create `descending` as a descending version of `numbers`
3. Sort `people` by the "age" field
"""


# ----- YOUR SOLUTION -----

words = ["Banana", "Egg", "Pineapple", "Kiwi", "Mango"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

by_length = None    # TODO: words sorted by length
descending = None   # TODO: numbers sorted descending
by_age = None       # TODO: people sorted by "age"

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert by_length == ["Egg", "Kiwi", "Mango", "Banana", "Pineapple"], (
        f"by_length → {by_length}"
    )
    assert descending == [9, 6, 5, 5, 4, 3, 2, 1, 1], f"descending → {descending}"
    assert [p["name"] for p in by_age] == ["Bob", "Alice", "Charlie"], (
        f"by_age → {[p['name'] for p in by_age]}"
    )
    print("✓ lists4 done!")
