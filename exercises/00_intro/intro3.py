# Topic: Introduction
# Exercise: intro3

"""
Type Conversion

In Python, values have different types:
- int    → whole numbers:    42, -7, 0
- float  → decimal numbers:  3.14, -0.5
- str    → strings:          "Hello", "42"
- bool   → booleans:         True, False

You can convert types with: int(), float(), str()

Your tasks:
1. Convert `age_text` to an integer (`age`)
2. Convert `price_text` to a float (`price`)
3. Calculate `total` = age + int(price)
"""



# ----- YOUR SOLUTION -----

age_text = "25"
price_text = "9.99"

age = None    # TODO: Convert age_text to int
price = None  # TODO: Convert price_text to float
total = None  # TODO: Calculate age + int(price)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert isinstance(age, int), f"age should be int, but got {type(age).__name__}"
    assert age == 25, f"age should be 25, but got {age}"
    assert isinstance(price, float), f"price should be float, but got {type(price).__name__}"
    assert abs(price - 9.99) < 0.001, f"price should be ~9.99, but got {price}"
    assert total == 34, f"total should be 34 (25 + 9), but got {total}"
    print("✓ intro3 done!")
