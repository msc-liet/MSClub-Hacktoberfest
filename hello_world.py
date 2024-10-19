def greet(name):
    print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            greet(name)
            break
        else:
            print("Name cannot be empty. Please try again.")
