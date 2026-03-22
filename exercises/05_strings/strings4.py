# Topic: Strings
# Exercise: strings4

"""
String Slicing

Just like with lists, you can use [start:stop:step] to cut out parts of a string:
    s = "Python"
    s[0]      → "P"      (first character)
    s[-1]     → "n"      (last character)
    s[0:3]    → "Pyt"    (index 0 to 2)
    s[2:]     → "thon"   (from index 2)
    s[:3]     → "Pyt"    (up to index 2)
    s[::-1]   → "nohtyP" (reversed)
    s[::2]    → "Pto"    (every second character)

Your tasks:
1. Implement `reversed_str(s)` → returns the string reversed (slicing only!)
2. Implement `every_other(s)` → returns every second character
3. Implement `is_palindrome(s)` → True if s reversed equals s
"""


# ----- YOUR SOLUTION -----

def reversed_str(s):
    # TODO: Use slicing s[::-1]
    pass


def every_other(s):
    # TODO: Use slicing s[::2]
    pass


def is_palindrome(s):
    # TODO: Compare s with s[::-1] (case-insensitive: s.lower())
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert reversed_str("Python") == "nohtyP"
    assert reversed_str("") == ""
    assert reversed_str("a") == "a"

    assert every_other("Python") == "Pto"
    assert every_other("abcdef") == "ace"

    assert is_palindrome("racecar") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("ELE") is True, "Ignore case"
    assert is_palindrome("") is True
    print("✓ strings4 done!")
