# Topic: Conditions
# Exercise: if_else3

"""
Logical Operators

In Python you combine conditions with:
    and  → both must be True
    or   → at least one must be True
    not  → inverts the truth value

Examples:
    age >= 18 and has_id        → adult AND has ID
    is_weekend or is_holiday    → weekend OR holiday
    not is_blocked              → NOT blocked

Your tasks:
1. Implement `may_vote(age, is_citizen)`:
   - True only when age >= 18 AND is_citizen is True
2. Implement `ticket_price(age, is_member)`:
   - Child (< 6): free → 0
   - Member: 5
   - Senior (>= 65): 8
   - Regular: 12
"""


# ----- YOUR SOLUTION -----

def may_vote(age, is_citizen):
    # TODO: Return True when age >= 18 AND is_citizen
    pass


def ticket_price(age, is_member):
    # TODO: Return the correct price
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert may_vote(20, True) is True
    assert may_vote(17, True) is False, "Too young"
    assert may_vote(20, False) is False, "Not a citizen"
    assert may_vote(16, False) is False

    assert ticket_price(3, False) == 0, "Child < 6 is free"
    assert ticket_price(25, True) == 5, "Members pay 5"
    assert ticket_price(70, False) == 8, "Seniors pay 8"
    assert ticket_price(30, False) == 12, "Regular: 12"
    assert ticket_price(5, False) == 0, "Child age 5: free"
    print("✓ if_else3 done!")
