def is_palindrome(s):
    # Normalize the string: convert to lower case and filter out non-alphanumeric characters
    normalized_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    length = len(normalized_s)
    for i in range(length // 2):
        if normalized_s[i] != normalized_s[length - 1 - i]:
            return False
            
    return True

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    if word.strip() == "":
        print("You did not enter a valid string.")
    else:
        print(f"'{word}' is a palindrome: {is_palindrome(word)}")
