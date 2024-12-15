# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

def goodbye():
    print("Goodbye, Hacktoberfest!")

def repeat_message(message, times):
    for _ in range(times):
        print(message)

def personalized_greet(name):
    print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    greet()  # Calls the greet function
    goodbye()  # Calls the goodbye function
    repeat_message("Keep coding!", 3)  # Repeats a message 3 times
    personalized_greet("Uzaafar")  # Greets the user with their name
