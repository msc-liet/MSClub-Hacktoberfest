# palindrome_checker.py

import re

def is_palindrome(s):
    # Normalize the string: lowercasing and removing non-alphanumeric characters
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f"'{word}' is a palindrome: {is_palindrome(word)}")

