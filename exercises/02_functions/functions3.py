# Topic: Functions
# Exercise: functions3

"""
Default Arguments

Parameters can have default values:
    def power(base, exponent=2):
        return base ** exponent

    power(3)     → 9   (exponent=2 is used)
    power(2, 10) → 1024

Important: Parameters with a default value come AFTER parameters without one!

Your tasks:
1. Implement `power(base, exponent=2)` → returns base^exponent
2. Implement `greeting(name, language="de")` → returns depending on language:
   - "de": "Hallo, {name}!"
   - "en": "Hello, {name}!"
   - "es": "¡Hola, {name}!"
"""


# ----- YOUR SOLUTION -----

def power(base, exponent=2):
    # TODO: Implement the function
    pass


def greeting(name, language="de"):
    # TODO: Return the correct greeting based on language
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    assert power(3) == 9, "power(3) should be 9 (3²)"
    assert power(2, 10) == 1024, "power(2, 10) should be 1024"
    assert power(5, 0) == 1, "power(5, 0) should be 1"

    assert greeting("Max") == "Hallo, Max!", f"greeting('Max') → {greeting('Max')!r}"
    assert greeting("Alice", "en") == "Hello, Alice!"
    assert greeting("Carlos", "es") == "¡Hola, Carlos!"
    print("✓ functions3 done!")
