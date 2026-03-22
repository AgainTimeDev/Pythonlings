# Topic: Lists
# Exercise: lists3

"""
List Slicing

Just like with strings, you can cut out parts of a list:
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data[0:3]   → [10, 20, 30]    (index 0 to 2)
    data[-3:]   → [80, 90, 100]   (last 3 elements)
    data[::2]   → [10, 30, 50, 70, 90]  (every second)
    data[::-1]  → [100, 90, ..., 10]    (reversed)
    data[2:8:2] → [30, 50, 70]   (from 2 to 7, every second)

Your tasks: Use slicing for each sub-task!
"""


# ----- YOUR SOLUTION -----

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_half = None    # TODO: First 5 elements
last_three = None    # TODO: Last 3 elements
every_other = None   # TODO: Every second element
reversed_list = None # TODO: List reversed
middle = None        # TODO: Elements from index 2 to 7 (inclusive)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert first_half == [10, 20, 30, 40, 50], f"first_half → {first_half}"
    assert last_three == [80, 90, 100], f"last_three → {last_three}"
    assert every_other == [10, 30, 50, 70, 90], f"every_other → {every_other}"
    assert reversed_list == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10], f"reversed_list → {reversed_list}"
    assert middle == [30, 40, 50, 60, 70, 80], f"middle → {middle}"
    print("✓ lists3 done!")
