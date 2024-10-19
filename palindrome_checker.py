def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    while True:
        word = input("Enter a word or phrase (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if not word.strip():
            print("Input cannot be empty. Please enter a valid word or phrase.")
            continue

        print(f"'{word}' is a palindrome: {is_palindrome(word)}")
