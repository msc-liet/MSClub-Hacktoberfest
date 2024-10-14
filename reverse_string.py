# reverse_string.py

# Existing reverse_string function
def reverse_string(s):
    return s[::-1]

# New function to reverse the order of words in a sentence
def reverse_words_in_sentence(s):
    words = s.split()  # Split the string into words
    reversed_words = ' '.join(reversed(words))  # Reverse the list of words and join them back into a string
    return reversed_words

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string (characters reversed): {reverse_string(string)}")
    print(f"Reversed string (words reversed): {reverse_words_in_sentence(string)}")
