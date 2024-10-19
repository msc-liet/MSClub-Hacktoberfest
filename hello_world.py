def greet(name):
    if not name.strip():  # Check for empty input
        print("Error: You must enter a name.")
    else:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)
