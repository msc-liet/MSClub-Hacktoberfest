def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def count_characters(s):
    return len(s)

def main():
    string = input("Enter a string: ")

    reversed_str = reverse_string(string)
    palindrome_check = is_palindrome(string)
    char_count = count_characters(string)

    print(f"Reversed string: {reversed_str}")
    print(f"Is the string a palindrome? {'Yes' if palindrome_check else 'No'}")
    print(f"Number of characters in the string: {char_count}")

if __name__ == "__main__":
    main()
