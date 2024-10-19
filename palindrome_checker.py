import re

def is_palindrome(s):
    # Normalize the string: convert to lowercase and remove non-alphanumeric characters
    normalized_str = re.sub(r'[^A-Za-z0-9]', '', s.lower())
    
    # Two-pointer technique
    left, right = 0, len(normalized_str) - 1
    while left < right:
        if normalized_str[left] != normalized_str[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    while True:
        string = input("Enter a string (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the program.")
            break
        else:
            if is_palindrome(string):
                print(f'"{string}" is a palindrome.')
            else:
                print(f'"{string}" is not a palindrome.')
