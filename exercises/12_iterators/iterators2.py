# Topic: Iterators
# Exercise: iterators2

"""
Custom Iterators

To make a class iterable, implement:
    __iter__(self)  → returns self
    __next__(self)  → returns next value or raise StopIteration

Example – numbers from start to end:
    class Range:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __iter__(self):
            return self

        def __next__(self):
            if self.current >= self.end:
                raise StopIteration
            value = self.current
            self.current += 1
            return value

Your task:
Implement `Countdown(start)`:
- Counts down from start to 0 (inclusive)
- for n in Countdown(3) → 3, 2, 1, 0
"""


# ----- YOUR SOLUTION -----

class Countdown:
    def __init__(self, start):
        # TODO: Start at `start`
        pass

    def __iter__(self):
        # TODO: return self
        pass

    def __next__(self):
        # TODO: Return current value and decrease it
        # If below 0: raise StopIteration
        pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    result = list(Countdown(5))
    assert result == [5, 4, 3, 2, 1, 0], f"Countdown(5) → {result}"

    result2 = list(Countdown(0))
    assert result2 == [0], f"Countdown(0) → {result2}"

    total = sum(Countdown(4))
    assert total == 10, f"0+1+2+3+4 = 10, got: {total}"
    print("✓ iterators2 done!")
