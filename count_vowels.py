def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)
    
    return vowel_count, consonant_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(string)
    
    print(f"Number of vowels in '{string}': {vowels}")
    print(f"Number of consonants in '{string}': {consonants}")
