# count_vowels.py
def count_vowels(s:str)->int:
    """Counts the number of vowels in a string.

    Args:
        s(str): The string to be parsed for vowels.

    Returns:
        The number of vowels in the specifed string. 
    """
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in s if char in vowels)
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Number of vowels in '{string}': {count_vowels(string)}")
