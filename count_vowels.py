def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    if string:  # Check if the string is not empty
        print(f"Number of vowels in '{string}': {count_vowels(string)}")
    else:
        print("You entered an empty string.")
