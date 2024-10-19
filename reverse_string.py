# reverse_string.py
def reverse_words(sentence):
    """Return the sentence with the order of words reversed."""
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    return ' '.join(reversed_words)  # Join the words back into a sentence

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Reversed words: {reverse_words(sentence)}")
