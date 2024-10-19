def greet(name):
    if name.strip():
        print(f"Hello, {name}! Welcome to Hacktoberfest!")
    else:
        print("You did not enter a name. Please provide a valid name.")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)

