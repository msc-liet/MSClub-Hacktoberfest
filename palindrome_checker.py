def greet(name):
    """Greet the user with their name."""
    print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    name = input("Please enter your name: ").strip()

    if not name:
        print("Error: You must enter a name.")
    else:
        greet(name)

