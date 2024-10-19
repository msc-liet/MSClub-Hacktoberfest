# reverse_string.py
def reverse_words(s):
    words = s.split()  # Split the string into words
    return ' '.join(reversed(words))  # Reverse the order of words and join them

if __name__ == "__main__":
    string = input("Enter a sentence: ")
    print(f"Reversed words: {reverse_words(string)}")

