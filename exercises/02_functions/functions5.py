# Topic: Functions
# Exercise: functions5

"""
Scope

Variables inside functions are local — they are only visible within the function.

To modify a global variable, you need the `global` keyword:
    counter = 0
    def increment():
        global counter
        counter += 1

For nested functions there is `nonlocal`:
    def outer():
        x = 0
        def inner():
            nonlocal x
            x += 1
        inner()
        return x  # → 1

Your tasks:
1. Fix `increment_counter()` — it should increment the global variable `counter`
2. Fix `create_counter()` — the inner function should be able to modify `count`
"""


# ----- YOUR SOLUTION -----

counter = 0

def increment_counter():
    # TODO: Increment the global variable `counter` by 1
    # (Tip: you need the `global` keyword)
    counter += 1  # This doesn't work yet — why?


def create_counter():
    count = 0
    def tick():
        # TODO: Increment the outer variable `count` by 1
        # (Tip: you need the `nonlocal` keyword)
        count += 1  # This doesn't work yet — why?
    tick()
    tick()
    tick()
    return count


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    increment_counter()
    increment_counter()
    assert counter == 2, f"counter should be 2, but got {counter}"

    result = create_counter()
    assert result == 3, f"create_counter() should return 3, but got {result}"
    print("✓ functions5 done!")
