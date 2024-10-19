# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
def reverse_string(s):
    return s[::-1]

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
    
    # Check for anagrams
    string1 = input("Enter the first string to check for anagrams: ")
    string2 = input("Enter the second string to check for anagrams: ")
    print(f"{string1} and {string2} are anagrams: {is_anagram(string1, string2)}")
    
    # Capitalize words
    text_to_capitalize = input("Enter a string to capitalize each word: ")
    print(f"Capitalized string: {capitalize_words(text_to_capitalize)}")
    
    # Count vowels
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
