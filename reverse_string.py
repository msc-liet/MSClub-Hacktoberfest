def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    while True:
        string = input("Enter a string to reverse (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if string:
            print(f"Reversed string: {reverse_string(string)}")
        else:
            print("Please enter a non-empty string.")
