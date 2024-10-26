# reverse_string.py
def reverse_string(s:str)->str:
    """Reverse a string.

    Args:
        s(str): The string to be reversed.

    Returns:
        The reversed string.
    """
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
