# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return consonants

def count_words(s):
    words = s.split()
    return len(words)

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
    print(f"Number of consonants in '{string}': {count_consonants(string)}")
    print(f"Number of words in '{string}': {count_words(string)}")
