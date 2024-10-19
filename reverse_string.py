def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def get_user_input():
    """Prompts the user for a string and validates the input."""
    while True:
        string = input("Enter a string (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Exiting the program.")
            return None
        elif string.strip():  # Check for non-empty input
            return string
        print("Please enter a non-empty string.")

if __name__ == "__main__":
    while True:
        string = get_user_input()
        if string is None:
            break
        print(f"Reversed string: {reverse_string(string)}")
