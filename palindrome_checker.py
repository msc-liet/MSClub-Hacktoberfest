# palindrome_checker.py
import string

def is_palindrome(s):
    return s == s[::-1]

def is_palindrome_phrase(phrase):
    # Remove punctuation and spaces, and convert to lowercase
    cleaned = ''.join(char.lower() for char in phrase if char.isalnum())
    return cleaned == cleaned[::-1]

def count_palindromic_words(sentence):
    words = sentence.split()
    return sum(1 for word in words if is_palindrome(word))

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
    
    phrase = input("Enter a phrase: ")
    print(f'"{phrase}" is a palindrome: {is_palindrome_phrase(phrase)}')
    
    sentence = input("Enter a sentence: ")
    palindromic_count = count_palindromic_words(sentence)
    print(f"Number of palindromic words in the sentence: {palindromic_count}")
