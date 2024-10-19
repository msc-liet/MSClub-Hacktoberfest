# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count
def count_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return consonants
if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
 vowel_count = count_vowels(string)
    consonant_count = count_consonants(string)
    
    print(f"Number of vowels in '{string}': {vowel_count}")
    print(f"Number of consonants in '{string}': {consonant_count}")

