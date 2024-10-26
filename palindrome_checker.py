# palindrome_checker.py
def is_palindrome(s:str)->bool:
    """Checks whether a string is a palindrome.

    Args:
        s(str): The string to be checked.

    Returns:
        Whether the string is a palindrome.
    """
    return s == s[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(f"{word} is a palindrome: {is_palindrome(word)}")
