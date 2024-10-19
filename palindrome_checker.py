def is_palindrome(s):
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move the left pointer to the right until we find an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move the right pointer to the left until we find an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare the characters, ignoring case
        if s[left].lower() != s[right].lower():
            return False
        
        # Move towards the center
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
 
