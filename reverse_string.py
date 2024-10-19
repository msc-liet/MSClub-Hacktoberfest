def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    if string:
        print(f"Reversed string: {reverse_string(string)}")
    else:
        print("You entered an empty string.")
# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Reversed string: {reverse_string(string)}")
