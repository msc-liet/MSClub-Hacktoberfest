# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is a prime number: {is_prime(num)}")
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
