# Topic: Variables
# Exercise: variables1

"""
Variable Assignment

In Python, variables are created by simple assignment.
No type declaration needed (no int x = 5 like in Java/C).

Valid variable names:
  ✓ name, age, my_value, _private, value2
  ✗ 2value (starts with digit), my-value (hyphen)

Your tasks:
1. Assign `name` the value "Alice"
2. Assign `age` the value 30
3. Assign `is_student` the value True
4. Assign `height` the value 1.75
"""


# ----- YOUR SOLUTION -----

name = None        # TODO: Set to "Alice"
age = None         # TODO: Set to 30
is_student = None  # TODO: Set to True
height = None      # TODO: Set to 1.75

# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert name == "Alice", f"name should be 'Alice', but got {name!r}"
    assert age == 30, f"age should be 30, but got {age}"
    assert is_student is True, f"is_student should be True, but got {is_student}"
    assert abs(height - 1.75) < 0.001, f"height should be 1.75, but got {height}"
    assert isinstance(name, str), "name should be a string"
    assert isinstance(age, int), "age should be an int"
    assert isinstance(is_student, bool), "is_student should be a bool"
    assert isinstance(height, float), "height should be a float"
    print("✓ variables1 done!")
