def reverse_string(s):
    return s[::-1]

def reverse_words_in_sentence(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    return ' '.join(reversed_words)  # Join them back into a sentence

if __name__ == "__main__":
    while True:
        string = input("Enter a string or sentence (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if not string:  # Check for empty input
            print("Input cannot be empty. Please enter a valid string.")
            continue

        print(f"Reversed string: {reverse_string(string)}")
        print(f"Reversed words in sentence: {reverse_words_in_sentence(string)}")
