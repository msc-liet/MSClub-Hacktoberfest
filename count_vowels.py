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
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return count

def get_vowel_positions(s):
    vowels = "aeiouAEIOU"
    positions = [i for i, char in enumerate(s) if char in vowels]
    return positions

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    no_vowels = ''.join(char for char in s if char not in vowels)
    return no_vowels

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    num_vowels = count_vowels(string)
    num_consonants = count_consonants(string)
    vowel_positions = get_vowel_positions(string)
    string_without_vowels = remove_vowels(string)
    
    print(f"Number of vowels in '{string}': {num_vowels}")
    print(f"Number of consonants in '{string}': {num_consonants}")
    print(f"Positions of vowels in '{string}': {vowel_positions}")
    print(f"String without vowels: '{string_without_vowels}'")
