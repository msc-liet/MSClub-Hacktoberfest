# hello_world.py
def greet():
    print("Hello, Hacktoberfest!")

def greet_user(name):
    print(f"Hello, {name}! Welcome to Hacktoberfest!")

def ask_favorite_language():
    language = input("What's your favorite programming language? ")
    print(f"Great choice! {language} is awesome!")

def ask_contribution_interest():
    interest = input("What type of contributions are you interested in? ")
    print(f"That's fantastic! Contributing to {interest} will be very rewarding.")

def goodbye():
    print("Thank you for visiting! Happy coding!")

if __name__ == "__main__":
    greet()
    user_name = input("Please enter your name: ").strip()
    
    if not user_name:
        print("Error: Name cannot be empty.")
    else:
        greet_user(user_name)
        ask_favorite_language()
        ask_contribution_interest()
        goodbye()
