def reverse_string(s):
    return s[::-1]

def reverse_words_in_sentence(sentence):
    # Split the sentence into words, reverse the order, and join back into a string
    return ' '.join(sentence.split()[::-1])

if __name__ == "__main__":
    while True:
        user_input = input("Enter a string to reverse (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break
        
        if not user_input:  # Check for empty input
            print("Error: You must enter a string.")
        else:
            reversed_str = reverse_string(user_input)
            reversed_words = reverse_words_in_sentence(user_input)
            print(f"Original string: {user_input}")
            print(f"Reversed string: {reversed_str}")
            print(f"Words reversed: {reversed_words}")
