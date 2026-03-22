# Topic: Dictionaries
# Exercise: dicts1

"""
Dictionary Basics

A dictionary (dict) stores key-value pairs:
    person = {"name": "Alice", "age": 30, "city": "Berlin"}
    person["name"]         → "Alice"
    person["age"] = 31     → change value
    person["country"] = "DE"  → add new entry
    del person["city"]     → delete entry
    "name" in person       → True (key present?)

Your tasks:
1. Create a phone book `phone_book` with three entries:
   "Alice": "0176-1234", "Bob": "0151-5678", "Charlie": "0160-9999"
2. Assign `alice_number` the number of Alice
3. Change Charlie's number to "0160-0000"
4. Add "Dave": "0172-4321"
5. Delete Bob from the phone book
"""


# ----- YOUR SOLUTION -----

# TODO: Create the phone book
phone_book = {}

# TODO: alice_number = phone_book["Alice"]
alice_number = None

# TODO: Change Charlie's number
# phone_book[???] = ???

# TODO: Add Dave

# TODO: Delete Bob

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert alice_number == "0176-1234", f"alice_number → {alice_number!r}"
    assert phone_book.get("Charlie") == "0160-0000", f"Charlie → {phone_book.get('Charlie')!r}"
    assert "Dave" in phone_book, "Dave is missing from the phone book"
    assert "Bob" not in phone_book, "Bob should have been deleted"
    assert len(phone_book) == 3, f"Phone book should have 3 entries, has {len(phone_book)}"
    print("✓ dicts1 done!")
