import re

def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lower case
    normalized_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return normalized_str == normalized_str[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    if word:
        print(f"{word} is a palindrome: {is_palindrome(word)}")
    else:
        print("You entered an empty string.")
# palindrome_checker.py
def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
