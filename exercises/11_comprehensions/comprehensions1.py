# Topic: Comprehensions
# Exercise: comprehensions1

"""
List Comprehensions

Instead of:
    squares = []
    for x in range(10):
        squares.append(x ** 2)

You can write:
    squares = [x ** 2 for x in range(10)]

General pattern:
    [expression for variable in iterable]

Your tasks:
Write each task as ONE line comprehension (not as a loop)!
1. `squares` = squares of numbers 0 to 9
2. `uppercase` = each word in UPPERCASE
3. `lengths` = length of each word
"""


# ----- YOUR SOLUTION -----

words = ["python", "was", "cool", "and", "makes", "rocks"]

squares = None    # TODO: [x**2 for x in range(10)]

uppercase = None  # TODO: [... for w in words]

lengths = None    # TODO: [len(...) for w in words]


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert uppercase == ["PYTHON", "WAS", "COOL", "AND", "MAKES", "ROCKS"]
    assert lengths == [6, 3, 4, 3, 5, 5]
    print("✓ comprehensions1 done!")
