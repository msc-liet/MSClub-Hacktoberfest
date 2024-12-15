def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in s if char in consonants)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowel_count = count_vowels(string)
    consonant_count = count_consonants(string)
    
    print(f"Number of vowels in '{string}': {vowel_count}")
    print(f"Number of consonants in '{string}': {consonant_count}")
    print(f"Summary: {vowel_count} vowels and {consonant_count} consonants in the input.")
