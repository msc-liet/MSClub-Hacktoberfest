def reverse_string(s):
    return s[::-1]

def main():
    string = input("Enter a string: ")
    
    # Trim whitespace and check for empty input
    if not string.strip():
        print("Please enter a non-empty string.")
    else:
        reversed_str = reverse_string(string)
        print(f"Reversed string: '{reversed_str}'")

if __name__ == "__main__":
    main()

