# Topic: Generators
# Exercise: generators1

"""
Generators and yield

A generator is a special function with yield.
It "pauses" after each yield and returns a value:
    def count():
        yield 1
        yield 2
        yield 3

    for n in count():
        print(n)  # 1, 2, 3

Generators are memory-efficient — they compute values only when needed!
Perfect for infinite sequences:
    def even_numbers():
        n = 0
        while True:
            yield n
            n += 2

Your tasks:
1. Implement `fibonacci()` — infinite generator of the Fibonacci sequence:
   0, 1, 1, 2, 3, 5, 8, 13, 21, ...
2. Implement `take(n, generator)` → list of the first n values
"""


# ----- YOUR SOLUTION -----

def fibonacci():
    # TODO: yield the Fibonacci sequence indefinitely
    # Tip: a, b = 0, 1; yield a; a, b = b, a+b
    pass


def take(n, generator):
    # TODO: Return list of the first n values from the generator
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    fib = take(10, fibonacci())
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], f"fib → {fib}"

    assert take(1, fibonacci()) == [0]
    assert take(0, fibonacci()) == []

    # Generators are lazy — only the first 5 are computed
    gen = fibonacci()
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 1
    print("✓ generators1 done!")
