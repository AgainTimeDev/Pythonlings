# Topic: Introduction
# Exercise: intro1

"""
Hello, Pythonlings!

Welcome to Pythonlings! Your first task is simple:
Set the variable `message` to the text "Hello, Pythonlings!".

Tip: Strings in Python are written in quotes:
    text = "This is how a string looks"
"""



# ----- YOUR SOLUTION -----

message = None  # TODO: Set message to "Hello, Pythonlings!"

print(message)

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert message == "Hello, Pythonlings!", (
        f"Expected: 'Hello, Pythonlings!', got: {message!r}"
    )
    print("✓ intro1 done!")
