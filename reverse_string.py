# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
# reverse_string.py
def reverse_string(s):
    return s[::-1]

def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())  # Ignore spaces and case
    return cleaned == reverse_string(cleaned)

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
    
    print(f"String with words reversed: {reverse_words(string)}")
    
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")
