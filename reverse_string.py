# reverse_string.py

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ").strip()  # Trim whitespace
    if string:  # Check if the string is not empty
        print(f"Reversed string: {reverse_string(string)}")
    else:
        print("Please enter a non-empty string.")

