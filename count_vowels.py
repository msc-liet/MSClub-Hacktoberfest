def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    num_vowels = count_vowels(string)
    num_consonants = count_consonants(string)
    print(f"Number of vowels in '{string}': {num_vowels}")
    print(f"Number of consonants in '{string}': {num_consonants}")
