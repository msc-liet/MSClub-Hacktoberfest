# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is {factorial(num)}")
# hello_world.py

def greet():
    print("Hello, Hacktoberfest!")

def ask_participation():
    print("Are you participating in Hacktoberfest?")

def share_resources():
    print("Check out the official website for resources: https://hacktoberfest.com")

def say_goodbye():
    print("Goodbye! See you at Hacktoberfest!")

if __name__ == "__main__":
    greet()
    ask_participation()
    share_resources()
    say_goodbye()
