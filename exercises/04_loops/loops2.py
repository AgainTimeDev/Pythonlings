# Topic: Loops
# Exercise: loops2

"""
for loop over lists

You can use for to iterate over any list:
    for fruit in ["Apple", "Banana", "Cherry"]:
        print(fruit)

Your tasks:
1. Implement `celsius_to_fahrenheit(temperatures)`:
   - Takes a list of Celsius values
   - Returns a new list with Fahrenheit values
   - Formula: fahrenheit = celsius * 9/5 + 32
2. Implement `count_words(sentences)`:
   - Takes a list of sentences (strings)
   - Returns a list with the word count per sentence
"""


# ----- YOUR SOLUTION -----

def celsius_to_fahrenheit(temperatures):
    # TODO: Convert each temperature and return the new list
    result = []
    for temp in temperatures:
        pass  # TODO: Calculate fahrenheit and append it to result
    return result


def count_words(sentences):
    # TODO: Count the words in each sentence and return a list of the counts
    # Tip: sentence.split() splits a sentence into words
    pass


# ----- TESTS (do not modify) -----

if __name__ == "__main__":
    result = celsius_to_fahrenheit([0, 100, -40])
    assert abs(result[0] - 32.0) < 0.01, f"0°C → 32°F, got: {result[0]}"
    assert abs(result[1] - 212.0) < 0.01, f"100°C → 212°F, got: {result[1]}"
    assert abs(result[2] - (-40.0)) < 0.01, "-40°C → -40°F"

    assert count_words(["Hello World", "Python is great", "Hi"]) == [2, 3, 1]
    assert count_words([]) == []
    print("✓ loops2 done!")
