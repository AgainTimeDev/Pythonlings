# Topic: Error Handling
# Exercise: error_handling2

"""
Multiple Exceptions and finally

You can catch multiple error types:
    try:
        ...
    except ValueError as e:
        print(f"Value error: {e}")
    except TypeError:
        print("Type error!")
    finally:
        print("Always runs!")  # runs on success AND on error

The finally block ALWAYS runs – ideal for cleanup.

Your tasks:
1. Implement `parse_input(data, key)`:
   - Access data[key] (can raise KeyError)
   - Convert the value to int (can raise ValueError)
   - Return the int value
   - On KeyError: return "Key missing"
   - On ValueError: return "Not a valid integer"
   - Set in finally: cleaned_up = True (global)
"""


# ----- YOUR SOLUTION -----

cleaned_up = False  # Should be set to True in finally


def parse_input(data, key):
    global cleaned_up
    # TODO: Implement try/except KeyError/ValueError/finally
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert parse_input({"x": "42"}, "x") == 42
    assert parse_input({"x": "abc"}, "x") == "Not a valid integer"
    assert parse_input({}, "x") == "Key missing"
    assert cleaned_up is True, "finally block was not executed!"
    print("✓ error_handling2 done!")
