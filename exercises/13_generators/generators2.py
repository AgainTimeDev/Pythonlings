# Topic: Generators
# Exercise: generators2

"""
Generator Expressions

Like list comprehensions, but with () instead of []:
    squares_list = [x**2 for x in range(10)]      # List (computed immediately)
    squares_gen  = (x**2 for x in range(10))      # Generator (lazy!)

Generators are great for large datasets:
    total = sum(x**2 for x in range(1_000_000))    # No memory issue!

Your tasks:
1. Create `even_gen` = generator expression for even numbers from 0 to 99
2. Implement `running_average()` — a generator that:
   - Receives new values via send()
   - Returns the current average
   - Returns None on the first next() call (initialization)
"""


# ----- YOUR SOLUTION -----

# TODO: Generator expression for even numbers 0-99
even_gen = None  # (x for x in range(100) if ...)


def running_average():
    # TODO: Generator with send() support
    # Pattern:
    #   total = 0
    #   count = 0
    #   value = yield None  # Initial initialization
    #   while True:
    #       total += value
    #       count += 1
    #       value = yield total / count
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    even_list = list(even_gen)
    assert even_list == list(range(0, 100, 2)), f"even_gen has {len(even_list)} elements"

    avg = running_average()
    next(avg)  # Initialization
    assert avg.send(10) == 10.0
    assert avg.send(20) == 15.0
    assert avg.send(30) == 20.0
    print("✓ generators2 done!")
