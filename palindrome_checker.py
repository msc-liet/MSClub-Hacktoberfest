# palindrome_checker.py
def is_palindrome(s):
    # Normalize the string by removing non-alphanumeric characters and converting to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    length = len(s)
    
    # Check for palindrome using two-pointer technique
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
