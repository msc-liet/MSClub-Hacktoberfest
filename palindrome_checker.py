# palindrome_checker.py
def is_palindrome(s):
    # Convert to lowercase to make the check case-insensitive
    s = s.lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
