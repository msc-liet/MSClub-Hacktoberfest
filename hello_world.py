# hello_world.py

def greet(name="Hacktoberfest"):
    """Print a greeting to the user."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name (or press Enter for default): ")
    greet(user_name or "Hacktoberfest")
