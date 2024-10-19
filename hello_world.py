def greet(name):
    if name:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")
    else:
        print("Hello! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    while True:
        name = input("Enter your name: ").strip()
        if name:
            greet(name)
            break
        else:
            print("Name cannot be empty. Please enter a valid name.")
