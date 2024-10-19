def is_palindrome(s):
    return s == s[::-1]

def clean_string(s):
    return ''.join(char.lower() for char in s if char.isalnum())

def check_palindrome():
    word = input("Enter a word or phrase: ")
    cleaned_word = clean_string(word)
    print(f"Cleaned input: {cleaned_word}")
    print(f"{word} is a palindrome: {is_palindrome(cleaned_word)}")

def main():
    check_palindrome()

if __name__ == "__main__":
    main()
