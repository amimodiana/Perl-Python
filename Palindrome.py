def is_palindrome(word):
    # Convert word to lowercase to make the check case-insensitive
    word = word.lower()
    # Check if the word reads the same forwards and backwards
    return word == word[::-1]
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

