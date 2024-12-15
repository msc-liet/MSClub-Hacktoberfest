def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    vowel_count = {vowel: s.count(vowel) for vowel in vowels}
    return count, vowel_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    if not string:  # Check for empty input
        print("Please enter a non-empty string.")
    else:
        total_count, detailed_count = count_vowels(string)
        print(f"Number of vowels in '{string}': {total_count}")
        print("Detailed count of each vowel:")
        for vowel, count in detailed_count.items():
            print(f"{vowel}: {count}")
