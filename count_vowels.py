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
    total_vowels, total_consonants = 
