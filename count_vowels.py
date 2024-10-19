def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    vowel_count = {vowel: s.count(vowel) for vowel in vowels}
    return count, vowel_count

def main():
    string = input("Enter a string: ").strip()
    
    if not string:
        print("Please enter a non-empty string.")
    else:
        total_count, detailed_count = count_vowels(string)
        print(f"Number of vowels in '{string}': {total_count}")
        print("Detailed count of each vowel:")
        for vowel in "aeiouAEIOU":
            print(f"{vowel}: {detailed_count[vowel]}")

if __name__ == "__main__":
    main()

