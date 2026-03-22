# Topic: Conditions
# Exercise: if_else2

"""
elif Chains

With elif (else if) you can check multiple conditions:
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Satisfactory"
    else:
        return "Failing"

Important: Conditions are checked from top to bottom.
Only the first matching block is executed.

Your task:
Implement `grade(points)`:
- 90-100: "Excellent"
- 80-89:  "Good"
- 70-79:  "Satisfactory"
- 60-69:  "Sufficient"
- 0-59:   "Failing"
"""


# ----- YOUR SOLUTION -----

def grade(points):
    # TODO: Return the appropriate grade
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert grade(95) == "Excellent", f"95 points → {grade(95)!r}"
    assert grade(85) == "Good"
    assert grade(75) == "Satisfactory"
    assert grade(65) == "Sufficient"
    assert grade(50) == "Failing"
    assert grade(90) == "Excellent", "Boundary value 90"
    assert grade(80) == "Good", "Boundary value 80"
    assert grade(60) == "Sufficient", "Boundary value 60"
    print("✓ if_else2 done!")
