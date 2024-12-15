# palindrome_checker.py
import re

def is_palindrome(s):
    return s == s[::-1]

def normalize_string(s):
    # Remove spaces and non-alphanumeric characters, and convert to lowercase
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def is_palindrome_phrase(phrase):
    normalized = normalize_string(phrase)
    return is_palindrome(normalized)

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
    print(f"{word} is a palindrome (normalized): {is_palindrome_phrase(word)}")
