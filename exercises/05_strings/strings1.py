# Topic: Strings
# Exercise: strings1

"""
String Basics

Strings can be created with ' or ".
Special characters are written with escape sequences:
    \n  → newline
    \t  → tab
    \\  → backslash
    \'  → single quote

With r"..." (raw string) backslashes are not treated as escape sequences:
    r"C:\new\test"  → C:\new\test  (not C:<newline>ew<tab>est)

Your tasks:
1. Create `path` as a raw string: C:\Users\new\test
2. Create `multiline` as a string with a newline after "Line 1"
3. Calculate `length` = length of "Pythonlings"
"""


# ----- YOUR SOLUTION -----

# TODO: Create path as a raw string with the value C:\Users\new\test
path = None

# TODO: Create multiline = "Line 1\nLine 2" (with an actual newline)
multiline = None

# TODO: Length of "Pythonlings"
length = None

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert path == r"C:\Users\new\test", f"path → {path!r}"
    assert "\n" in multiline, "multiline must contain a newline"
    assert multiline.startswith("Line 1"), "Must start with 'Line 1'"
    assert length == 11, f"'Pythonlings' has 11 characters, got: {length}"
    print("✓ strings1 done!")
