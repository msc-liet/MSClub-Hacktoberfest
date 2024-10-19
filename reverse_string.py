def reverse_string(s):
    return s[::-1]

def reverse_words(s):
    return ' '.join(reversed(s.split()))

if __name__ == "__main__":
    while True:
        string = input("Enter a string (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        print(f"Reversed string: {reverse_string(string)}")
        
        choice = input("Would you like to reverse the order of the words instead? (y/n): ").strip().lower()
        if choice == 'y':
            print(f"Reversed word order: {reverse_words(string)}")
