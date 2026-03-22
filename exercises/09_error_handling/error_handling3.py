# Topic: Error Handling
# Exercise: error_handling3

"""
Custom Exceptions and raise

With raise you can trigger exceptions yourself:
    def check_age(age):
        if age < 0:
            raise ValueError(f"Age cannot be negative: {age}")

Custom exception classes inherit from Exception:
    class MyError(Exception):
        pass

    class ErrorWithCode(Exception):
        def __init__(self, message, code):
            super().__init__(message)
            self.code = code

Your tasks:
1. Implement `validate_age(age)`:
   - Raises ValueError if age < 0 or age > 150
   - Returns age if valid
2. Define `AccountError(Exception)` with attribute `account_number`
3. Implement `withdraw(account_number, balance, amount)`:
   - Raises AccountError if amount > balance
   - Returns new balance
"""


# ----- YOUR SOLUTION -----

def validate_age(age):
    # TODO: raise ValueError if age < 0 or > 150
    pass


class AccountError(Exception):
    # TODO: __init__(self, message, account_number)
    pass


def withdraw(account_number, balance, amount):
    # TODO: Raise AccountError if amount > balance
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert validate_age(25) == 25
    assert validate_age(0) == 0

    try:
        validate_age(-1)
        assert False, "Expected ValueError!"
    except ValueError as e:
        assert "-1" in str(e) or "negative" in str(e).lower() or "0" in str(e)

    try:
        validate_age(200)
        assert False, "Expected ValueError!"
    except ValueError:
        pass

    assert withdraw("DE123", 1000, 200) == 800

    try:
        withdraw("DE456", 100, 500)
        assert False, "Expected AccountError!"
    except AccountError as e:
        assert e.account_number == "DE456", f"account_number → {e.account_number!r}"

    print("✓ error_handling3 done!")
