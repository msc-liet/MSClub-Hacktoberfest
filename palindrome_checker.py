# palindrome_checker.py
import re

def is_palindrome(s: str) -> bool:
    # Normalize the string: remove non-alphanumeric characters and convert to lower case
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f'"{word}" is a palindrome: {is_palindrome(word)}')
