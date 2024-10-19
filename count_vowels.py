# count_vowels.py

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in s if char in consonants)
    return count

def count_total_characters(s):
    return len(s)

def to_uppercase(s):
    return s.upper()

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
    print(f"Number of consonants in '{string}': {count_consonants(string)}")
    print(f"Total number of characters in '{string}': {count_total_characters(string)}")
    print(f"Uppercase version of the string: '{to_uppercase(string)}'")
