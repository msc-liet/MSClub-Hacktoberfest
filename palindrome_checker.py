import re

def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # Early exit for trivial cases
    if len(normalized_s) <= 1:
        return True
    
    # Check for palindrome
    left, right = 0, len(normalized_s) - 1
    while left < right:
        if normalized_s[left] != normalized_s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
