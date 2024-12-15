def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string to reverse: ").strip()
    if not string:
        print("You entered an empty string. Please provide a valid string.")
    else:
        print(f"Reversed string: {reverse_string(string)}")

