# Topic: Loops
# Exercise: loops5

"""
enumerate() and zip()

enumerate() returns both index AND value:
    for i, value in enumerate(["a", "b", "c"]):
        print(i, value)  # 0 a, 1 b, 2 c

zip() combines two lists:
    for name, score in zip(["Alice", "Bob"], [1, 2]):
        print(name, score)

Your tasks:
1. Implement `format_results(names, scores)`:
   - Use zip() to pair names and scores
   - Return a list of strings: "Place 1: Alice - 85 Points"
   - Use enumerate() for the rank number (starts at 1)
2. Implement `index_of_max(lst)` → returns the index of the largest element
   (without using max() directly with key — use enumerate!)
"""


# ----- YOUR SOLUTION -----

def format_results(names, scores):
    # TODO: Use enumerate(zip(names, scores), start=1) or similar
    pass


def index_of_max(lst):
    # TODO: Find the index of the largest element using enumerate()
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    result = format_results(names, scores)
    assert result[0] == "Place 1: Alice - 85 Points", f"→ {result[0]!r}"
    assert result[1] == "Place 2: Bob - 92 Points"
    assert result[2] == "Place 3: Charlie - 78 Points"

    assert index_of_max([3, 1, 4, 1, 5, 9, 2, 6]) == 5, "Index of 9 is 5"
    assert index_of_max([1]) == 0
    print("✓ loops5 done!")
