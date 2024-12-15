def reverse_string(s):
    return s[::-1]

def reverse_words_in_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the order of words
    return ' '.join(reversed_words)  # Join them back into a string

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")

    sentence = input("Enter a sentence: ")
    print(f"Sentence with reversed word order: {reverse_words_in_sentence(sentence)}")
