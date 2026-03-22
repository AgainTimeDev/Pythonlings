# Topic: Comprehensions
# Exercise: comprehensions3

"""
Dict and Set Comprehensions

Dict comprehension:
    {key: value for ... in ...}
    {word: len(word) for word in words}

Set comprehension (like list, but with {} — no duplicates!):
    {x % 3 for x in range(10)}  → {0, 1, 2}

Your tasks:
1. `word_lengths` = Dict: word → length
2. `first_letters` = set of first letters of all words
3. Implement `group_by_length(words)`:
   - Returns dict: {length: [words with that length]}
   - Use a regular loop + dict (comprehension is too complex here)
"""


# ----- YOUR SOLUTION -----

words = ["Apple", "Banana", "Pineapple", "Pear", "On", "Bo", "Avocado"]

word_lengths = None    # TODO: {word: len(word) for word in words}

first_letters = None   # TODO: {word[0] for word in words}


def group_by_length(words):
    # TODO: Return {length: [list of words]} dict
    # Tip: Use .get(length, []) to check if the key already exists
    result = {}
    for word in words:
        pass  # TODO
    return result


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert word_lengths["Apple"] == 5
    assert word_lengths["On"] == 2
    assert isinstance(word_lengths, dict)

    assert isinstance(first_letters, set)
    assert "A" in first_letters
    assert "B" in first_letters

    groups = group_by_length(["On", "Bo", "Apple", "Grape", "Lemon"])
    assert sorted(groups[2]) == ["Bo", "On"]
    assert sorted(groups[5]) == ["Apple", "Grape", "Lemon"]
    print("✓ comprehensions3 done!")
