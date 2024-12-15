# reverse_string.py
def reverse_string(s):
    return s[::-1]

def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = ' '.join(words[::-1])  # Reverse the order of words and join them
    return reversed_words

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    # Reverse the entire string
    print(f"Reversed string: {reverse_string(string)}")
    
    # Reverse the words in the sentence
    print(f"Reversed words: {reverse_words(string)}")
