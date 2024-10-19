# reverse_string.py

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
    print(f"Is the string a palindrome? {'Yes' if is_palindrome(string) else 'No'}")
    print(f"Number of vowels in the string: {count_vowels(string)}")
