def is_palindrome(s):
    """Checks if a given string is a palindrome."""
    return s == s[::-1]

def normalize_input(s):
    """Normalizes the input by removing spaces and converting to lowercase."""
    return ''.join(s.split()).lower()

def get_user_input():
    """Prompts the user for a word and validates the input."""
    while True:
        word = input("Enter a word (or 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the program.")
            return None
        if word.strip():
            return word
        print("Please enter a non-empty word.")

if __name__ == "__main__":
    while True:
        word = get_user_input()
        if word is None:
            break
        normalized_word = normalize_input(word)
        print(f"{word} is a palindrome: {is_palindrome(normalized_word)}")
