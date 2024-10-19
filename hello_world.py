# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

if __name__ == "__main__":
    greet()
def greet(name="Hacktoberfest"):
    """Greets the specified name."""
    print(f"Hello, {name}!")

def greet_multiple(names):
    """Greets a list of names."""
    for name in names:
        greet(name)

def count_greetings(names):
    """Returns the count of names in the list."""
    return len(names)

def ask_for_name():
    """Prompts the user for a name and returns it."""
    name = input("Enter your name: ")
    return name

def main():
    # Default greeting
    greet()
    
    # Custom greeting from user
    name = ask_for_name()
    greet(name)

    # Greet a list of predefined names
    names_list = ["Alice", "Bob", "Charlie"]
    greet_multiple(names_list)

    # Count greetings
    count = count_greetings(names_list)
    print(f"Total greetings: {count}")

if __name__ == "__main__":
    main()
