# Topic: Loops
# Exercise: loops4

"""
break and continue

With break you exit a loop early:
    for i in range(10):
        if i == 5:
            break  # loop ends at i=5

With continue you skip to the next iteration:
    for i in range(10):
        if i % 2 == 0:
            continue  # skip even numbers
        print(i)  # prints only odd numbers

Your tasks:
1. Implement `first_negative(lst)` → returns the first negative number
   (or None if none exists)
2. Implement `without_multiples(n, limit)` → returns a list from 1..limit,
   without multiples of n
"""


# ----- YOUR SOLUTION -----

def first_negative(lst):
    # TODO: Iterate over the list, return the first negative number
    # Use break! If none found: return None
    pass


def without_multiples(n, limit):
    # TODO: Return a list from 1..limit, skipping multiples of n
    # Tip: use continue when num % n == 0
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert first_negative([1, 2, -3, 4, -5]) == -3
    assert first_negative([1, 2, 3]) is None
    assert first_negative([-1, -2, -3]) == -1

    assert without_multiples(3, 10) == [1, 2, 4, 5, 7, 8, 10], f"→ {without_multiples(3, 10)}"
    assert without_multiples(2, 6) == [1, 3, 5]
    print("✓ loops4 done!")
