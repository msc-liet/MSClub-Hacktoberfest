def greet():
    print("Hello, Hacktoberfest!")

def greet_user(name):
    if not name.strip():
        print("Error: You must enter a name.")
    else:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")

def get_user_input():
    return input("Please enter your name: ")

def main():
    greet()
    name = get_user_input()
    greet_user(name)

if __name__ == "__main__":
    main()
