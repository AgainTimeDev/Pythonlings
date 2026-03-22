# Topic: Strings
# Exercise: strings2

"""
String Methods

Strings have many useful methods:
    " hello ".strip()        → "hello"        (remove whitespace)
    "hello".upper()          → "HELLO"
    "HELLO".lower()          → "hello"
    "hello world".title()    → "Hello World"
    "a,b,c".split(",")       → ["a", "b", "c"]
    ",".join(["a","b","c"])  → "a,b,c"
    "hello".replace("l","r") → "herro"
    "hello".startswith("he") → True
    "hello".count("l")       → 2

Your tasks:
1. Implement `normalize(s)` → strip whitespace + Title Case
2. Implement `count_vowels(s)` → count of vowels (a,e,i,o,u, upper and lower case)
3. Implement `swap_ends(s)` → swap the first and last character
"""


# ----- YOUR SOLUTION -----

def normalize(s):
    # TODO: strip() + title()
    pass


def count_vowels(s):
    # TODO: Count all vowels in s (a, e, i, o, u – upper and lower case)
    pass


def swap_ends(s):
    # TODO: Swap the first and last character
    # Tip: s[0], s[-1], s[1:-1]
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert normalize("  hello world  ") == "Hello World"
    assert normalize("  python  ") == "Python"

    assert count_vowels("Hello") == 2, f"'Hello' has 2 vowels: {count_vowels('Hello')}"
    assert count_vowels("Python") == 1
    assert count_vowels("Rhythms") == 1
    assert count_vowels("") == 0

    assert swap_ends("Python") == "nythoP", f"swap_ends('Python') → {swap_ends('Python')!r}"
    assert swap_ends("ab") == "ba"
    assert swap_ends("a") == "a"
    print("✓ strings2 done!")
