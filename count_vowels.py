# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in s if char in consonants)
    return count

def count_vowels_and_consonants(s):
    return count_vowels(s), count_consonants(s)

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowel_count = count_vowels(string)
    consonant_count = count_consonants(string)
    total_vowels, total_consonants = count_vowels_and_consonants(string)

    print(f"Number of vowels in '{string}': {vowel_count}")
    print(f"Number of consonants in '{string}': {consonant_count}")
    print(f"Total vowels and consonants in '{string}': Vowels: {
