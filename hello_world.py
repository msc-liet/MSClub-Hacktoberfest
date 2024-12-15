# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

if __name__ == "__main__":
    greet()
from datetime import datetime

def greet(message="Hello, Hacktoberfest!"):
    print(message)

def greet_multiple_times(message, times):
    for _ in range(times):
        greet(message)

def greet_with_name(name):
    greet(f"Hello, {name}! Welcome to Hacktoberfest!")

def display_current_datetime():
    now = datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    greet()  # Default greeting
    custom_message = input("Enter a custom greeting (or press Enter for default): ")
    if custom_message:
        greet(custom_message)
    
    # Greet with name
    name = input("What is your name? ")
    greet_with_name(name)

    # Greet multiple times
    times = int(input("How many times would you like to greet? "))
    greet_multiple_times(custom_message or "Hello, Hacktoberfest!", times)

    # Display current date and time
    display_current_datetime()

if __name__ == "__main__":
    main()
