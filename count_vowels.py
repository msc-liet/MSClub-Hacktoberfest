def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowel_count = count_vowels(string)
    consonant_count = count_consonants(string)
    
    print(f"Number of vowels in '{string}': {vowel_count}")
    print(f"Number of consonants in '{string}': {consonant_count}")
