# hello_world.py

def greet(name):
    if not name.strip():
        print("Error: Name cannot be empty. Please provide a valid name.")
    else:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greet(user_name)

