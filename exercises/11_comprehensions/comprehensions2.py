# Topic: Comprehensions
# Exercise: comprehensions2

"""
Filtered and Nested Comprehensions

With if you can filter elements:
    [x for x in range(20) if x % 2 == 0]  → even numbers

Nested comprehensions (for 2D data):
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    flat = [num for row in matrix for num in row]
    → [1, 2, 3, 4, 5, 6, 7, 8, 9]

Your tasks:
1. `even_squares` = squares of 0-99, only the even ones
2. `long_words` = words with more than 4 letters (from words)
3. `flat` = the nested matrix as a flat list
"""


# ----- YOUR SOLUTION -----

words = ["Apple", "Egg", "Banana", "Kiwi", "Cherry", "Lime"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

even_squares = None  # TODO: squares of 0-99 that are even

long_words = None    # TODO: words with len > 4

flat = None          # TODO: matrix as flat list


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert even_squares == [0, 4, 16, 36, 64], f"even_squares → {even_squares}"
    assert long_words == ["Apple", "Banana", "Cherry"], f"long_words → {long_words}"
    assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("✓ comprehensions2 done!")
