# Topic: Variables
# Exercise: variables3

"""
Checking Types

With type() you can determine the type of a variable:
    type(42)        → <class 'int'>
    type("Hello")   → <class 'str'>

With isinstance() you check whether a value has a certain type:
    isinstance(42, int)    → True
    isinstance(42, float)  → False

Your tasks:
1. Determine the type of `secret` with type() and assign it to `secret_type`
2. Check with isinstance() whether `number` is an int → `is_integer`
3. Check with isinstance() whether `text` is a str → `is_string`
"""


# ----- YOUR SOLUTION -----

secret = 3.14
number = 42
text = "Python"

secret_type = None  # TODO: type(secret)
is_integer = None   # TODO: isinstance(number, int)
is_string = None    # TODO: isinstance(text, str)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert secret_type == float, f"secret_type should be float, but got {secret_type}"
    assert is_integer is True, "is_integer should be True"
    assert is_string is True, "is_string should be True"
    assert not isinstance(secret, int), "3.14 is not an int!"
    print("✓ variables3 done!")
