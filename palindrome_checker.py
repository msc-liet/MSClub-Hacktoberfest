def is_palindrome(s):
    # Normalize the string: convert to lowercase and filter out non-alphanumeric characters
    filtered_s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Use two-pointer technique to check for palindrome
    left, right = 0, len(filtered_s) - 1
    while left < right:
        if filtered_s[left] != filtered_s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
