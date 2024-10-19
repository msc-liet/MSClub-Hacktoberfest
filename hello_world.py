def greet(name):
    if name.strip():  # Check if the input is not empty or just whitespace
        print(f"Hello, {name}! Welcome to Hacktoberfest!")
    else:
        print("Error: You must enter a name.")

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greet(user_name)
