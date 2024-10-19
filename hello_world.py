def greet(name):
    if name:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")
    else:
        print("You didn't enter a name. Please try again.")

if __name__ == "__main__":
    name = input("Enter your name: ").strip()  # Remove leading/trailing whitespace
    greet(name)
