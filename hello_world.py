# hello_world.py
def greet(name):
    """Prints a greeting message to the user."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = input("Please enter your name: ").strip()  # Get user input and remove extra spaces
    if not name:  # Check if the input is empty
        print("Error: Name cannot be empty.")
    else:
        greet(name)
