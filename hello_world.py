def greet(name="Hacktoberfest"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name (or press Enter for 'Hacktoberfest'): ")
    greet(user_name if user_name else "Hacktoberfest")
# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

if __name__ == "__main__":
    greet()
