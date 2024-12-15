def greet():
    name = input("Please enter your name: ").strip()
    
    if not name:
        print("Error: You must enter a name.")
    else:
        print(f"Hello, {name}! Happy Hacktoberfest!")

if __name__ == "__main__":
    greet()

