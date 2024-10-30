def greet(name="Hacktoberfest"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name (or press Enter for default): ")
    if user_name.strip() == "":
        greet()  # Calls greet with default name
    else:
        greet(user_name)  # Calls greet with user-provided name
