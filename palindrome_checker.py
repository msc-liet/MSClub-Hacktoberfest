import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
