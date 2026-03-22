# Topic: Iterators
# Exercise: iterators1

"""
iter() and next()

In Python every for-loop is internally an iterator:
    it = iter([1, 2, 3])  # Creates iterator
    next(it)  → 1
    next(it)  → 2
    next(it)  → 3
    next(it)  → StopIteration (end!)

With a default value you can avoid StopIteration:
    next(it, "End")  → "End" instead of error

Your tasks:
1. Use iter() and next() to get the first 3 elements from `numbers`
   (without a loop, without indexing!)
2. Implement `nth_element(iterable, n)`:
   - Returns the n-th element (0-based)
   - Without indexing (use iter/next)
   - Returns None if not available
"""


# ----- YOUR SOLUTION -----

numbers = [10, 20, 30, 40, 50]

# TODO: Create iterator and get first 3 elements with next()
it = None    # iter(numbers)
first = None   # next(it)
second = None  # next(it)
third = None   # next(it)


def nth_element(iterable, n):
    # TODO: Use iter() and call next() n+1 times
    # Tip: for _ in range(n): next(it, None)
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert first == 10, f"first → {first}"
    assert second == 20
    assert third == 30

    assert nth_element([1, 2, 3, 4, 5], 0) == 1
    assert nth_element([1, 2, 3, 4, 5], 4) == 5
    assert nth_element([1, 2, 3], 10) is None, "Index too large → None"
    assert nth_element("Python", 2) == "t"
    print("✓ iterators1 done!")
