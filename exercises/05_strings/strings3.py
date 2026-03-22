# Topic: Strings
# Exercise: strings3

"""
f-Strings (Formatted Strings)

f-strings allow embedding expressions inside strings:
    name = "Alice"
    age = 30
    f"I am {name} and {age} years old."
    → "I am Alice and 30 years old."

Formatting options:
    f"{3.14159:.2f}"    → "3.14"       (2 decimal places)
    f"{42:05d}"         → "00042"      (5 digits with leading zeros)
    f"{0.75:.0%}"       → "75%"        (percent)
    f"{'left':<10}"     → "left      " (left-aligned, 10 characters)

Your tasks: Create the f-strings exactly as specified.
"""


# ----- YOUR SOLUTION -----

name = "Max"
age = 25
height = 1.823
score = 0.876

# TODO: "Max is 25 years old and 1.82 m tall."
introduction = None  # f"..."

# TODO: "Score: 87.6%"
score_str = None     # f"..."

# TODO: "Result: 025" (3 digits, leading zeros)
result_str = None    # f"..."

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert introduction == "Max is 25 years old and 1.82 m tall.", (
        f"introduction → {introduction!r}"
    )
    assert score_str == "Score: 87.6%", f"score_str → {score_str!r}"
    assert result_str == "Result: 025", f"result_str → {result_str!r}"
    print("✓ strings3 done!")
