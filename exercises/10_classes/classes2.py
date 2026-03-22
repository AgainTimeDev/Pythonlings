# Topic: Classes
# Exercise: classes2

"""
Class vs. Instance Attributes

Class attributes belong to the class (shared by all objects):
    class Dog:
        species = "Canis lupus familiaris"  # class attribute
        count = 0

        def __init__(self, name):
            self.name = name  # instance attribute
            Dog.count += 1

    d1 = Dog("Rex")
    d2 = Dog("Bello")
    Dog.species  → "Canis lupus familiaris"  (for all)
    Dog.count    → 2

Your tasks:
Extend the class `Account`:
1. Class attribute `interest_rate = 0.02` (2%)
2. `__init__(self, owner, balance=0)` – store owner and balance
3. Method `deposit(amount)` – increase balance by amount
4. Method `withdraw(amount)` – decrease balance by amount
5. Method `calculate_interest()` – return balance * interest_rate
"""


# ----- YOUR SOLUTION -----

class Account:
    interest_rate = None  # TODO: Set to 0.02

    def __init__(self, owner, balance=0):
        # TODO: Set self.owner and self.balance
        pass

    def deposit(self, amount):
        # TODO: Increase balance
        pass

    def withdraw(self, amount):
        # TODO: Decrease balance
        pass

    def calculate_interest(self):
        # TODO: Return balance * interest_rate
        pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    a = Account("Alice", 1000)
    assert a.owner == "Alice"
    assert a.balance == 1000
    assert Account.interest_rate == 0.02

    a.deposit(500)
    assert a.balance == 1500

    a.withdraw(200)
    assert a.balance == 1300

    assert abs(a.calculate_interest() - 26.0) < 0.001, "1300 * 0.02 = 26.0"
    print("✓ classes2 done!")
