# Character Frequency Analysis (Naive Approach)
# Using only lists and loops
# Only counts letters(case-sensitive) and spaces, Ignores punctuation

def char_frequency(sentence):
    """
    Question 4. Think:
    In my code, I use a loop to go through each character in the sentence,
    and for each character, I use another loop to count how many times it appears in the entire sentence.
    Because there are two loops nested inside each other, the total steps get bigger about (sentence length) × (sentence length)
    That’s why the time complexity is O(n^2). For example, if the sentence has 10,000 characters, the code has to do about 10,000 × 10,000 checks.
    """
    result = []  # This will store tuples in the list

    for char in sentence:
        # Only count letters and spaces
        if not (char.isalpha() or char == " "):
            continue  # Skip punctuation or other characters(digits, special characters,etc.)

        # Check if we've already counted this character
        already_counted = False
        for pair in result:          # pair = (char, count)
            if pair[0] == char:
                already_counted = True
                break
        if already_counted:
            continue        # Skip the rest and go to the next character

        # Count occurrences of this character
        count = 0
        for c in sentence:
            if c == char:
                count += 1

        result.append((char, count))  # Store as tuple (char, count)

    return result


# Output
text = input("Enter a sentence: ")
freq_result = char_frequency(text)

print("Character frequencies (letters and spaces only):")
for pair in freq_result:
    print(f"{pair[0]}: {pair[1]}")
