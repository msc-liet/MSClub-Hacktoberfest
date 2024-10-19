# count_vowels.py
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)

def count_digits(s):
    return sum(1 for char in s if char.isdigit())

def count_special_characters(s):
    return sum(1 for char in s if not char.isalnum() and not char.isspace())

def count_vowels_and_consonants(s):
    return count_vowels(s), count_consonants(s)

def count_vowel_frequency(s):
    vowels = "aeiouAEIOU"
    frequency = {vowel: s.lower().count(vowel) for vowel in vowels}
    return frequency

def calculate_vowel_percentage(s):
    total_letters = count_vowels(s) + count_consonants(s)
    return (count_vowels(s) / total_letters * 100) if total_letters > 0 else 0

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    # Count vowels
    vowel_count = count_vowels(string)
    print(f"Number of vowels in '{string}': {vowel_count}")

    # Count consonants
    consonant_count = count_consonants(string)
    print(f"Number of consonants in '{string}': {consonant_count}")

    # Count digits
    digit_count = count_digits(string)
    print(f"Number of digits in '{string}': {digit_count}")

    # Count special characters
    special_char_count = count_special_characters(string)
    print(f"Number of special characters in '{string}': {special_char_count}")

    # Count vowels and consonants together
    total_vowels, total_consonants = count_vowels_and_consonants(string)
    print(f"Total vowels: {total_vowels}, Total consonants: {total_consonants}")

    # Count vowel frequency
    vowel_freq = count_vowel_frequency(string)
    print(f"Vowel frequency: {vowel_freq}")

    # Calculate vowel percentage
    vowel_percentage = calculate_vowel_percentage(string)
    print(f"Percentage of vowels: {vowel_percentage:.2f}%")
