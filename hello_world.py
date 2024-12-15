def greet(name="Hacktoberfest"):
    """Greets the user with a specified name."""
    print(f"Hello, {name}!")

def get_user_name():
    """Prompts the user for their name and validates the input."""
    while True:
        name = input("What's your name? ").strip()
        if name:
            return name
        print("You didn't enter a name. Please try again.")

if __name__ == "__main__":
    user_name = get_user_name()
    greet(user_name)
