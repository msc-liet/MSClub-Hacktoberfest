# hello_world.py

def greet():
    print("Hello, Hacktoberfest!")

def get_user_name():
    name = input("Please enter your name: ").strip()
    if not name:
        print("Error: You must enter a name!")
        return None
    return name

def farewell(name):
    if name:
        print(f"Goodbye, {name}! Have a great day!")

if __name__ == "__main__":
    greet()
    user_name = get_user_name()
    farewell(user_name)
