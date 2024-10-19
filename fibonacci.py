# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence: {fibonacci(n)}")
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
