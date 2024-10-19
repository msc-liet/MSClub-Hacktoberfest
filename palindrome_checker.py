# palindrome_checker.py
def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
import string

def is_palindrome(s):
    return s == s[::-1]

def is_palindrome_phrase(phrase):
    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    return is_palindrome(cleaned_phrase)

def count_palindromes(words):
    return sum(1 for word in words if is_palindrome(word))

def longest_palindrome(words):
    palindromes = [word for word in words if is_palindrome(word)]
    return max(palindromes, key=len) if palindromes else None

def is_numeric_palindrome(n):
    n_str = str(n)
    return is_palindrome(n_str)

def generate_palindrome(word):
    return word + word[::-1]

def list_all_palindromes(words):
    return [word for word in words if is_palindrome(word)]

if __name__ == "__main__":
    # Check for single word palindrome
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")

    # Check for phrase palindrome
    phrase = input("Enter a phrase: ")
    print(f'"{phrase}" is a palindrome: {is_palindrome_phrase(phrase)}')

    # Count palindromes in a list
    words_list = input("Enter a list of words (comma-separated): ").split(',')
    words_list = [word.strip() for word in words_list]
    print(f"Number of palindromes in the list: {count_palindromes(words_list)}")

    # Find the longest palindrome
    longest = longest_palindrome(words_list)
    if longest:
        print(f"The longest palindrome in the list is: {longest}")
    else:
        print("No palindromes found in the list.")

    # Check for numeric palindrome
    number = input("Enter a number to check if it is a palindrome: ")
    print(f"{number} is a numeric palindrome: {is_numeric_palindrome(number)}")

    # Generate a palindrome from a word
    word_to_palindrome = input("Enter a word to generate a palindrome: ")
    print(f"The generated palindrome is: {generate_palindrome(word_to_palindrome)}")

    # List all palindromes from the input list
    all_palindromes = list_all_palindromes(words_list)
    print(f"Palindromes in the list: {all_palindromes}")
    
